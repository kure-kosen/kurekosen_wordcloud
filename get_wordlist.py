import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import MeCab as mc
import re
import time
from urllib.parse import urljoin

def mecab_analysis(text):
    t = mc.Tagger('-Ochasen')
    t.parse('')
    node = t.parseToNode(text)
    output = []
    while(node):
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

def get_wordlist_from_QiitaURL(url):
    res = requests.get(url)
    if not res.status_code == 200:
        return []

    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    [script.extract() for script in soup.find_all("script")]
    [style.extract() for style in soup.find_all("style")]

    if soup.body == None:
        return []
    
    text = soup.body.get_text().replace('\n','').replace('\t','')
    return mecab_analysis(text)

def main():
    with open("url.txt", "r") as url_file:
        url = url_file.readline()

        while url:
            url = url.replace("\n", '')
            print(url)

            wordlist = get_wordlist_from_QiitaURL(url)
            if not len(wordlist) == 0:
                with open("wordlist/" + url.replace("/", "|") + ".txt", "w") as word_file:
                    word_file.write(" ".join(wordlist))
                    time.sleep(1)

            url = url_file.readline()

if __name__ == '__main__':
    main()
