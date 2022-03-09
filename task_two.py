import os
import re as regexp

# uncomment when start first time

# import nltk
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download("stopwords")
# nltk.download('wordnet')

from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


input_dir_path = 'output/task_one/'
output_dir_path = 'output/task_two/'
english = 'english'
read_file = 'r'
write_file = 'w'
new_line = '\n'
space_symbol = ' '
html_extension = '.html'
string_empty = ''
lemmas_txt = '_lemmas.txt'
tokens_txt = '_tokens.txt'
encoding = 'ISO-8859-1'


def clean_text(file_data):
    pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'
    file_data = regexp.sub(pattern, space_symbol, file_data,
                           flags=(regexp.IGNORECASE | regexp.MULTILINE | regexp.DOTALL))
    pattern = r'<[ ]*style.*?\/[ ]*style[ ]*>'
    file_data = regexp.sub(pattern, space_symbol, file_data,
                           flags=(regexp.IGNORECASE | regexp.MULTILINE | regexp.DOTALL))
    pattern = r'<[ ]*meta.*?>'
    file_data = regexp.sub(pattern, space_symbol, file_data,
                           flags=(regexp.IGNORECASE | regexp.MULTILINE | regexp.DOTALL))
    pattern = regexp.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    output = regexp.sub(pattern, space_symbol, file_data)
    return output


def get_words_from_sentence(sentence):
    sentence = sentence.lower()
    sentence = regexp.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+://\S+)|^rt|http.+?",
                          space_symbol,
                          sentence)
    sentence = regexp.sub(r"\d+", space_symbol, sentence)
    sentence = '  '.join([w for w in sentence.split() if w not in stopwords.words(english)])
    result = sentence.split()
    return result


print('START')
input_files = os.listdir(input_dir_path)
for file in input_files:
    with open(input_dir_path + file, read_file, encoding=encoding) as input_file:
        tokens = []
        lemmas = {}
        cleaned_text = clean_text(input_file.read())
        lines = [cleaned_text]
        if cleaned_text.find(new_line) != -1:
            lines = cleaned_text.split(new_line)
            for line in lines:
                if line:
                    sentences = sent_tokenize(line, language=english)
                    for se in sentences:
                        words = get_words_from_sentence(se)
                        for word in words:
                            current_lemma = WordNetLemmatizer().lemmatize(word)
                            if word not in tokens:
                                tokens.append(word)
                            if current_lemma not in lemmas:
                                lemmas[current_lemma] = set()
                            lemmas[current_lemma].add(word)
        with open(output_dir_path + file.replace(html_extension, string_empty) + tokens_txt, write_file) as output_file:
            for token in tokens:
                output_file.write(token + new_line)
        with open(output_dir_path + file.replace(html_extension, string_empty) + lemmas_txt, write_file) as output_file:
            for key, values in lemmas.items():
                lemma = key + space_symbol
                if len(values) <= 1:
                    lemma += key
                else:
                    for value in values:
                        lemma += value + space_symbol
                output_file.write(lemma + new_line)
print('END')
