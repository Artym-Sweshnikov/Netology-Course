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


class Document:
    """Класс Документы."""

    def identifier(self):
        """Метод для проверки пользовательского ввода."""
        id_vk_user = input('Введите ID или Username пользователя вк: ')
        if id_vk_user.isdigit() is True and len(id_vk_user) == 9:
            return id_vk_user
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
                    return id_vk_user

    def interrogate(self, identification):
        """Метод запрашивает данные c сервера и возвращает список фотографий."""

        def largest(size_dict):
            """Функция находит картинук максимального размера."""
            if size_dict['width'] >= size_dict['height']:
                return size_dict['width']
            else:
                return size_dict['height']

        response_vk = requests.get(
            'https://api.vk.com/method/photos.get',
            params={
                'access_token': TOKEN_VK,
                'owner_id': identification,
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
        return response_list[:5]

    def folder(self, identification):
        """Метод для создания директории на Яндекс.Диск"""
        response_searcher = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': TOKEN_VK,
                'user_ids': identification,
                'lang': 0,
                'v': 5.122
            }
        )
        for response in response_searcher.json()['response']:
            last_name = response['last_name']
            headers = {'Authorization': TOKEN_YANDEX}
            response_ya_disk = requests.put(
                'https://cloud-api.yandex.net/v1/disk/resources',
                headers=headers,
                params={
                    'path': last_name
                })
            return last_name

    def designate(self, dictionary):
        """Метод возвращает словарь с новыми именами"""
        name = []
        dates = []
        name_dict = []
        for picture in dictionary:
            likes = str(picture['like'])
            date_time = picture['date']
            date = datetime.fromtimestamp(date_time)
            date = date.strftime('%d.%m.%Y-%H:%M:%S')
            name.append(likes)
            dates.append(date)
        length = len(name)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if name[i] == name[j]:
                    name[i] += dates[i]
                    name[j] += dates[j]
        for index, image in enumerate(dictionary):
            image['photo']['name'] = [score
                                      for thing, score in enumerate(name) if thing == index]
            indicator = image['photo']['name'][0]
            image['photo']['name'] = indicator
        return dictionary

    def upload(self, new_dictionary, path):
        """Метод загружает фотографии на диск"""
        for picture in tqdm(new_dictionary, desc='Download Photos', unit='photo', dynamic_ncols=True, leave=False):
            name = str(picture['photo']['name']) + '.jpg'
            url = picture['photo']['url']
            headers = {'Authorization': TOKEN_YANDEX}
            response_ya_disk = requests.post(
                'https://cloud-api.yandex.net/v1/disk/resources/upload',
                headers=headers,
                params={
                    'url': url,
                    'path': f'/{path}/' + name
                })
            sleep(.1)
        print('Файлы успешно загруженны на Яндекс.Диск\n>>>', 'https://disk.yandex.ru/client/disk')

    def json_file(self, result_dictionary):
        """Метод создает json"""
        result_list = []
        for image in result_dictionary:
            result = {'file_name': image['photo']['name'], 'size': image['photo']['type']}
            result_list.append(result)
        with open('result.json', 'w') as file:
            json.dump(result_list, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    photo = Document()
    ID = photo.identifier()
    data = photo.interrogate(ID)
    disk_path = photo.folder(ID)
    new_names_dict = photo.designate(data)
    photo.upload(new_names_dict, disk_path)
    photo.json_file(new_names_dict)
