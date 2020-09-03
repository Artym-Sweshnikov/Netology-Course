import requests
import file as fl

keys_dict = fl.function()
token = keys_dict['API_KEY']


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        headers = {'Authorization': token}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params={'path': self.file_path})
        response_json = response.json()
        requests.put(response_json['href'])
        print('Success!')


if __name__ == '__main__':
    uploader = YaUploader('/Folder/file153.txt')
    result = uploader.upload()
