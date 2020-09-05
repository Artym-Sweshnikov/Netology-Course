import requests

name_list = ['Hulk', 'Captain_America', 'Thanos']
traits_list = []

for hero in name_list:
    response = requests.get('https://superheroapi.com/api/2619421814940190/search/' + hero)
    dict_results = response.json()['results']
    for value in dict_results:
        traits_list.append([value['name'], value['powerstats']['intelligence']])

print(max(traits_list, key=lambda x: int(x[1])))
