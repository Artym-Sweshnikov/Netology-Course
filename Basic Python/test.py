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


def create_folder(name_folder):
    '''Создает новую директорию на Яндекс.Диск.

    Папке присваевается имя id пользователя в вк.'''
    headers = {'Authorization': TOKEN_YANDEX}
    response_ya_disk = requests.put(
        'https://cloud-api.yandex.net/v1/disk/resources',
        headers=headers,
        params={
            'path': name_folder
        })


def upload(name, URL):
    '''Загружает полученные фотографии на Диск.

    Принимает только URL путь файла.'''
    print(name, URL)
    headers = {'Authorization': TOKEN_YANDEX}
    response_ya_disk = requests.post(
        'https://cloud-api.yandex.net/v1/disk/resources/upload',
        headers=headers,
        params={
            'url': URL,
            'path': f'/{folder_name(id_vk_user)}/' + name
        })


def get_largest(size_dict):
    '''Находит картинук максимального размера.

    Для сравнения подаются итерируемые объекты.'''
    if size_dict['width'] >= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']


def search_id(user_input):
    '''Ищем id пользователя в вк.

    Проверяем правильность пользовательский ввода.'''
    if user_input.isdigit() is True and len(user_input) == 9:
        return user_input
    else:
        response_searcher = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': TOKEN_VK,
                'user_ids': user_input,
                'v': 5.122
            }
        )
        for i in response_searcher.json()['response']:
            return i['id']


def folder_name(user_input):
    '''Называет директорию.

    Присваеват директории имя пользователя.'''
    response_searcher = requests.get(
        'https://api.vk.com/method/users.get',
        params={
            'access_token': TOKEN_VK,
            'user_ids': user_input,
            'lang': 0,
            'v': 5.122
        }
    )
    for i in response_searcher.json()['response']:
        return i['last_name']


def photo_name(element):
    for el in element:
        image = str(el['likes']['count']) + '.jpg'
        if image in name_list:
            ts = int(el['date'])
            name_list.append(image[:-4] + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d%H:%M:%S') + '.jpg')
        else:
            name_list.append(image)  # Добавляем имя фотографии в формате jpg


def json_file():
    '''Создает json файл.

    Файл сохраняется в директории запущенной программы.'''
    result_list = []
    for result_name, result_size in zip(name_list[0:5], type_list[0:5]):
        result = {'file_name': result_name, 'size': result_size}
        result_list.append(result)
    with open('photos.json', 'w') as file:
        json.dump(result_list, file, indent=2, ensure_ascii=False)


url_list = []
name_list = []
type_list = []

id_vk_user = input('Введите ID или Username пользователя вк: ')

response_vk = requests.get(
    'https://api.vk.com/method/photos.get',
    params={
        'access_token': TOKEN_VK,
        'owner_id': search_id(id_vk_user),
        'album_id': 'profile',
        'rev': 1,
        'extended': 1,
        'photo_sizes': 1,
        'v': 5.122
    }
)

# Преобразуем полученные данные с API VK в списки
data = response_vk.json()
photo_list = data['response']['items']
photo_name(photo_list)
for photo in photo_list:
    sizes = photo['sizes']
    max_size = max(sizes, key=get_largest)
    url_list.append(max_size['url'])  # Добавляем URL фотографий
    type_photo = max_size['type']
    type_list.append(type_photo)  # Добавляем тип фотографий

# Объеденяем полученные списки с именем фотографий и их URL в один словарь не более 5 элементов
photo_name_dict = dict(zip(name_list[0:5], url_list[0:5]))
# Создаём новую директорию на Яндекс.Диск
create_folder(folder_name(id_vk_user))
# Внедряем прогресс бар для отслеживания результата загрузки фотографий
for key, value in tqdm(photo_name_dict.items(), desc='Download Photos',
                       unit='photo', dynamic_ncols=True, leave=True):
    upload(key, value)
    sleep(.1)
json_file()
print('https://disk.yandex.ru/client/disk')
