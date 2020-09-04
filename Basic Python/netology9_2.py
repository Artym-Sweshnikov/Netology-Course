import requests
import file as fl

keys_dict = fl.function()
token = keys_dict['API_KEY']


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        file_name = self.file_path.split('/')[-1]
        headers = {'Authorization': token}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                headers=headers, params={'path': file_name})
        response_json = response.json()
        with open(self.file_path, 'rb') as f:
            requests.put(response_json['href'], files={'file': f})
        print('Success!')


if __name__ == '__main__':
    uploader = YaUploader('/Users/user/Documents/HTML/test.html')
    result = uploader.upload()
