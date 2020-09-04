from pprint import pprint
import requests

response = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
pprint(response)
dict_results = response.json()['results']
pprint(dict_results)
print(5)