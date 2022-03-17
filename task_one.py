import urllib
import urllib.request as urllib2
from bs4 import *
from urllib.parse import urljoin

result_urls = set()
file_index = 0
index_file_path = 'output/task_one/index.txt'
output_documents_path = 'output/task_one/'
write_mode = 'w'
features_parse_mode = 'html.parser'
href_code = 'href'
http_code = 'http'


def crawler(pages):
    indexed_url = []
    for page in pages:
        if page not in indexed_url:
            indexed_url.append(page)
            try:
                c = urllib2.urlopen(page)
            except:
                continue
            beautiful_soup = BeautifulSoup(c.read(), features=features_parse_mode)
            links = beautiful_soup('a')
            for link in links:
                if href_code in dict(link.attrs):
                    base_url = urljoin(page, link[href_code])
                    if base_url.find("'") != -1:
                        continue
                    base_url = base_url.split('#')[0]
                    if base_url[0:4] == http_code:
                        indexed_url.append(base_url)
    indexed_url = [iterator for iterator in indexed_url if 'chechnya' in iterator
                   or 'president' in iterator or 'russia' in iterator or 'politic' in iterator or 'dagestan' in iterator]
    return indexed_url


print("START")
result_urls.add('https://en.wikipedia.org/wiki/Ramzan_Kadyrov')
while len(result_urls) < 100:
    for i in list(result_urls):
        urls = crawler([i])
        result_urls.update(urls)
        if len(result_urls) > 100:
            break
    if len(result_urls) > 100:
        break
print("SAVE TO FILE")
with open(index_file_path, write_mode) as index_file:
    for url in result_urls:
        file_index += 1
        name = output_documents_path + str(file_index) + '.html'
        try:
            urllib.request.urlretrieve(url, name)
            result_string = str(file_index) + ')' + url.replace("\n", "") + '\n'
            index_file.write(result_string)
            if file_index == 100:
                index_file.close()
                break
        except:
            continue

print("END")
