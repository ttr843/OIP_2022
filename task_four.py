import glob
import math
import collections
import json

tokens_files_list = glob.glob("output/task_two/*_tokens.txt")

tokens_map = {}
tokens_data_count = {}


def calculate_idf_value(current_word):
    return math.log10(len(tokens_map) / tokens_data_count[current_word])


def calculate_tf_value(current_text):
    tf_texts = collections.Counter(current_text)
    for txt in tf_texts:
        tf_texts[txt] = tf_texts[txt] / float(len(current_text))
    return tf_texts


with open('output/task_three/inverted_index_2.txt', 'r') as f:
    data = f.readlines()
    for item in data:
        item = item.replace("\'", "\"")
        str_data = json.loads(item)
        tokens_data_count[str_data['word']] = str_data['count']

for file in tokens_files_list:
    with open(file, 'r') as fs:
        data = fs.read()
        data_list = data.splitlines()
        name = file.replace("_tokens.txt", "").replace("output/task_two/", "")
        tokens_map[name] = data_list


for key, value in tokens_map.items():
    tf_idf_map = {}
    calculated_tf = calculate_tf_value(value)
    for word in calculated_tf:
        idf = calculate_idf_value(word)
        tf_idf_map[word] = [idf, calculated_tf[word] * idf]
    with open('output/task_four_term/' + key + '_term.txt', 'w') as f:
        for key1, value1 in tf_idf_map.items():
            result = key1 + " " + str(value1[0]) + " " + str(value1[1])
            f.write("%s\n" % result)

lemmas_files_list = glob.glob("output/task_two/*_lemmas.txt")
lemmas_map = {}

for file in lemmas_files_list:
    with open(file, 'r') as fs:
        data = fs.read()
        data_list = data.splitlines()
        name = file.replace("_lemmas.txt", "").replace("output/task_two/", "")
        lemmas_map[name] = data_list

for key, value in tokens_map.items():
    tf_idf_map = {}
    calculated_tf = calculate_tf_value(value)
    current_lemmas = lemmas_map[key]
    for lemma in current_lemmas:
        values = lemma.split(' ')
        tf_lemma_sum = float(0)
        idf_sum = float(0)
        for i in range(1, len(values) - 1):
            tf_lemma_sum += calculated_tf[values[i]]
            idf_sum += calculate_idf_value(values[i])
        tf_idf_map[values[0].replace(":", "")] = [idf_sum, tf_lemma_sum * idf_sum]
    with open('output/task_four_lemmas/' + key + '_lemma.txt', 'w') as f:
        for key1, value1 in tf_idf_map.items():
            result = key1 + " " + str(value1[0]) + " " + str(value1[1])
            f.write("%s\n" % result)
