import requests
import file as fl
from pprint import pprint
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
    headers = {'Authorization': TOKEN_YANDEX}
    response_ya_disk = requests.post(
        'https://cloud-api.yandex.net/v1/disk/resources/upload',
        headers=headers,
        params={
            'url': URL,
            'path': f'/{id_vk_user}/' + name
        })


def get_largest(size_dict):
    '''Находит картинук максимального размера.

    Для сравнения подаются итерируемые объекты.'''
    if size_dict['width'] >= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']


url_list = []
name_list = []
type_list = []
result_dict = []

id_vk_user = input('Введите ID пользователя вк: ')

response_vk = requests.get(
    'https://api.vk.com/method/photos.get',
    params={
        'access_token': TOKEN_VK,
        'owner_id': id_vk_user,
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
for photo in photo_list:
    name_list.append(str(photo['likes']['count']) + '.jpg')  # Добавляем имя фотографии в формате jpg
    sizes = photo['sizes']
    max_size = max(sizes, key=get_largest)
    url_list.append(max_size['url'])  # Добавляем URL фотографий
    type_photo = max_size['type']
    type_list.append(type_photo)  # Добавляем тип фотографий

# Объеденяем полученные списки с именем фотографий и их URL в один словарь не более 5 элементов
photo_name_dict = dict(zip(name_list[0:5], url_list[0:5]))
# Создаём новую директорию на Яндекс.Диск
create_folder(id_vk_user)
# Внедряем прогресс бар для отслеживания результата загрузки фотографий
for key, value in tqdm(photo_name_dict.items(), desc='Download Photos',
                       unit='photo', dynamic_ncols=True, leave=True):
    upload(key, value)
    sleep(.1)
# Создаём конечный словарь с результатом загруженных фотографий на Яндекс.Диск
for result_name, result_size in zip(name_list[0:5], type_list[0:5]):
    result = {'file_name': result_name, 'size': result_size}
    result_dict.append(result)

print('https://disk.yandex.ru/client/disk')
pprint(result_dict)
