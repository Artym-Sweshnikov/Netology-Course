import xml.etree.ElementTree as ET
import operator

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

new_list = root.findall('channel/item')
words_list_more_six = []

for news in new_list:
    description = news.find('description').text
    list_of_word = (description.split(' '))
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
