import os
import nltk
import math
import glob
import json
import sys

nltk.download('omw-1.4')
nltk.download("stopwords")

from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

stop_words_eng = stopwords.words('english')
tokens_files_list = glob.glob("output/task_two/*_tokens.txt")


def calculate_differences_between_vectors(first_vector, second_vector):
  first_sum = 0
  second_sum = 0
  third_sum = 0

  for file in tokens_files_list:
    with open(file, 'r') as fs:
      data = fs.read()
      data_list = data.splitlines()
      for token in data_list:
        first_sum = first_sum + first_vector[token] * second_vector[token]
        second_sum = second_sum + first_vector[token] * first_vector[token]
        third_sum = third_sum + second_vector[token] * second_vector[token]

  if first_sum == 0 or second_sum == 0 or third_sum == 0:
    return 0
  return first_sum/(math.sqrt(second_sum) * math.sqrt(third_sum))


def calculate_vector(file_name):
  vector_map = {}
  file = open("output/task_four_lemmas/" + file_name)
  vecotor_values = file.read().split("\n")
  file.close()

  for vecotor_string in vecotor_values:
    if vecotor_string != "":
      vector_map[vecotor_string.split(" ")[0]] = float(vecotor_string.split(" ")[2])

  return vector_map

def proccessQuery(search_term):
  tokens_set = set()
  dictionary = {}
  vector_map = {}

  for file in tokens_files_list:
    with open(file, 'r') as fs:
      data = fs.read()
      data_list = data.splitlines()
      for token in data_list:
        dictionary[token] = 0

  search_term = '  '.join([word for word in search_term.split() if word not in (stop_words_eng)])
  words = search_term.split()
  for word in words:
    current_lemma = WordNetLemmatizer().lemmatize(word)
    tokens_set.add(current_lemma)
    dictionary[word] = dictionary[word] + 1

  for file in tokens_files_list:
    with open(file, 'r') as fs:
      data = fs.read()
      data_list = data.splitlines()
      for token in data_list:
        vector_map[token] = 0

  for token in tokens_set:
    vector_map[token] = dictionary[token] / float(len(words))

  result_map = {}
  lemmas_files = os.listdir("output/task_four_lemmas")
  for name in lemmas_files:
    print(calculate_vector(name))
    print(vector_map)
    print('\n')
    result_map[name] = calculate_differences_between_vectors(calculate_vector(name), vector_map)
  return result_map


sys.stdout.write(json.dumps((proccessQuery(sys.argv[1]))))

