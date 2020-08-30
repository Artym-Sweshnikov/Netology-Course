import json
import operator

with open('newsafr.json', 'r') as f:
    json_data = json.load(f)
words_list_more_six = []
list_of_articles = json_data['rss']['channel']['items']

for article in list_of_articles:
    text = (article['description'])
    list_of_word = (text.split(' '))
    for word in list_of_word:
        if len(word) > 6:
            words_list_more_six.append(word)

result = {i: words_list_more_six.count(i) for i in words_list_more_six}
sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
top_ten_common_words = sorted_result[0:10]
number = 0
for key, value in top_ten_common_words:
    number += 1
    print(number, key.capitalize())
