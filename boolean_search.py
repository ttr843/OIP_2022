import json
import re

requests = ['putin & story']
token_corpuses = {}
index_url = {}

with open('output/task_three/inverted_index_2.txt', 'r') as fs:
    data = fs.readlines()
    for elem in data:
        elem = elem.replace("\'", "\"")
        string_data = json.loads(elem)
        print(string_data)
        token_corpuses[string_data['word']] = string_data['inverted_array']


with open('output/task_one2/index.txt', 'r') as fs:
    data = fs.readlines()
    for elem in data:
        res = re.split('\)', elem)
        index_url[res[0]] = res[1].replace("\n", "")


for i in requests:
    result = set()
    links = []
    res = re.split('&', i)
    for r in res:
        r = r.strip()
        if len(result) == 0:
            result.update(token_corpuses[r])
        else:
            result = result.intersection(token_corpuses[r])
    for res in result:
        links.append(index_url[res])
    print("\n")
    print("Boolean request: " + i)
    print("Results: " + str(links))
    print("Results size: " + str(len(links)))
