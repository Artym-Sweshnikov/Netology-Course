import requests
import json
import file as fl
from pprint import pprint
from datetime import datetime
from tqdm import tqdm
from time import sleep

keys_dict = fl.function()
TOKEN_YANDEX = keys_dict['APP_YANDEX']
TOKEN_VK = keys_dict['APP_VK']


class User:
    """Класс Пользователь."""
    name = ''


class VkUser(User):
    """Подкласс Пользователь ВК"""
    ID = ''
    photo = ''

    def identifier(self):
        """Метод для проверки пользовательского ввода."""
        id_vk_user = input('Введите ID или Username пользователя вк: ')
        if id_vk_user.isdigit() is True and len(id_vk_user) == 9:
            self.ID = id_vk_user
        else:
            response_searcher = requests.get(
                'https://api.vk.com/method/users.get',
                params={
                    'access_token': TOKEN_VK,
                    'user_ids': id_vk_user,
                    'v': 5.122
                }
            )
            response_list = response_searcher.json()
            for response in response_list:
                if 'error' in response:
                    print('Вы ввели неверное имя пользователя')
                    quit()
                else:
                    id_vk_user = response['response']['id']
                    self.ID = id_vk_user

    def designate(self):
        """Метод получает имя Пользователя."""
        response_searcher = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': TOKEN_VK,
                'user_ids': self.ID,
                'lang': 0,
                'v': 5.122
            }
        )
        for response in response_searcher.json()['response']:
            full_name = response['first_name'] + ' ' + response['last_name']
            self.name = full_name
            return self.name

    def interrogate(self):
        """Метод запрашивает данные c сервера и возвращает список фотографий."""

        def largest(size_dict):
            """Функция находит картинук максимального размера."""
            if size_dict['width'] >= size_dict['height']:
                return size_dict['width']
            else:
                return size_dict['height']

        def rename(dictionary):
            """Функция переименовывает фотографии"""
            names = []
            dates = []
            for picture in dictionary:
                likes = str(picture['like'])
                date_time = picture['date']
                date = datetime.fromtimestamp(date_time)
                date = date.strftime('%d.%m.%Y')
                names.append(likes)
                dates.append(date)
            length = len(names)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if names[i] == names[j]:
                        names[i] += dates[i]
                        names[j] += dates[j]
            for index, image in enumerate(dictionary):
                image['photo']['name'] = [score
                                          for thing, score in enumerate(names) if thing == index]
                indicator = image['photo']['name'][0]
                image['photo']['name'] = indicator
            self.photo = dictionary

        response_vk = requests.get(
            'https://api.vk.com/method/photos.get',
            params={
                'access_token': TOKEN_VK,
                'owner_id': self.ID,
                'album_id': 'profile',
                'rev': 1,
                'extended': 1,
                'photo_sizes': 1,
                'v': 5.122
            }
        )

        response_list = []
        database = response_vk.json()
        photo_list = database['response']['items']
        for photos in photo_list:
            date = photos['date']
            sizes = photos['sizes']
            max_size = max(sizes, key=largest)
            response_dict = {'date': date, 'like': photos['likes']['count'], 'photo': dict(max_size)}
            response_list.append(response_dict)
        rename(response_list[:5])
        return self.photo


class YandexUser(User):
    """Подкласс Пользователь Яндекс."""

    def __init__(self, path, data):
        self.path = path
        self.data = data

    def folder(self):
        """Метод для создания директории на Яндекс.Диск"""
        headers = {'Authorization': TOKEN_YANDEX}
        requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            headers=headers,
            params={
                'path': self.path
            })

    def upload(self):
        """Метод загружает фотографии на диск"""
        for picture in tqdm(self.data, desc='Download Photos', unit='photo', dynamic_ncols=True, leave=False):
            codec = str(picture['photo']['name']) + '.jpg'
            url = picture['photo']['url']
            headers = {'Authorization': TOKEN_YANDEX}
            requests.post(
                'https://cloud-api.yandex.net/v1/disk/resources/upload',
                headers=headers,
                params={
                    'url': url,
                    'path': f'/{self.path}/' + codec
                })
            sleep(.1)
        print('Файлы успешно загруженны на Яндекс.Диск\n>>>', 'https://disk.yandex.ru/client/disk')

    def json_file(self):
        """Метод создает json"""
        result_list = []
        for image in self.data:
            result = {'file_name': image['photo']['name'] + '.jpg', 'size': image['photo']['type']}
            result_list.append(result)
        with open('result.json', 'w') as file:
            json.dump(result_list, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    user1 = VkUser()
    user1.identifier()
    name = user1.designate()
    photo = user1.interrogate()
    user1_yandex = YandexUser(name, photo)
    user1_yandex.folder()
    user1_yandex.upload()
    user1_yandex.json_file()
