import nltk
import math
import os
import glob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download("stopwords")

nltk.download('wordnet')
tokens_files_list = glob.glob("output/task_two/*_tokens.txt")

stop = stopwords.words('english')


def compare_vectors(vector1, vector2):
    sum = 0
    sum_two = 0
    sum_three = 0
    for token in vector1.keys():
        sum = sum + vector1[token] * vector2[token]
        sum_two = sum_two + vector1[token] * vector1[token]
        sum_three = sum_three + vector2[token] * vector2[token]
    if sum == 0 or sum_two == 0 or sum_three == 0:
        return 0
    return sum / (math.sqrt(sum_two) * math.sqrt(sum_three))


def get_vector_from_file(name):
    vector_dict = {}
    file = open("output/task_four_lemmas/" + name)
    vector_strings = file.read().split("\n")
    file.close()
    for vector_string in vector_strings:
        if vector_string != "":
            vector_dict[vector_string.split(" ")[0]] = float(vector_string.split(" ")[1])
    return vector_dict


def search(search_term):
    tokens_set = set()
    dictionary = {}
    vector_dict = {}
    tokens = set()
    for file in tokens_files_list:
        with open(file, 'r') as fs:
            for line in fs:
                tokens.add(WordNetLemmatizer().lemmatize(line[:-1]))
        fs.close()
    for token in tokens:
        dictionary[WordNetLemmatizer().lemmatize(token)] = 0
    search_term = '  '.join([word for word in search_term.split() if word not in stop])
    words = search_term.split()
    for word in words:
        current_lemma = WordNetLemmatizer().lemmatize(word)
        tokens_set.add(current_lemma)
        dictionary[word] = dictionary[word] + 1
    for token in tokens:
        vector_dict[token] = 0
    for token in tokens_set:
        vector_dict[token] = dictionary[token] / float(len(words))
    result_dict = {}
    vectors_files = os.listdir("output/task_four_lemmas")
    for name in vectors_files:
        result_dict[name] = compare_vectors(get_vector_from_file(name), vector_dict)
    return result_dict

