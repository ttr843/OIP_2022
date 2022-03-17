import glob

token_values = glob.glob("output/task_two/*_tokens.txt")
token_unique = set()
token_map = {}
result_map = {}

for file in token_values:
    with open(file, 'r') as fs:
        value = fs.read()
        split_value = value.splitlines()
        name = file.replace("_tokens.txt", "").replace("output/task_two/", "")
        token_unique.update(split_value)
        token_map[name] = split_value


for token in token_unique:
    result_map[token] = []
    for key, value in token_map.items():
        if token in value:
            result_map[token].append(key)


with open('output/task_three/inverted_index.txt', 'w') as fs:
    for key, values in result_map.items():
        result = key + " "
        for value in values:
            result += value + " "
        fs.write("%s\n" % result)


with open('output/task_three/inverted_index_2.txt', 'w') as fs:
    for key, values in result_map.items():
        result = {"count": len(values), "inverted_array": values, "word": key}
        fs.write("%s\n" % str(result))

