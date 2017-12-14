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
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.body.get_text().replace('\n','').replace('\t','')
    return mecab_analysis(text)

def create_wordcloud(text):

    # 環境に合わせてフォントのパスを指定する。
    #fpath = "/System/Library/Fonts/HelveticaNeue-UltraLight.otf"
    fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

    # ストップワードの設定
    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して',
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て', 'に', 'を', 'は', 'の', 'が', 'と', 'た', 'し', 'で',
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', '']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, stopwords=set(stop_words)).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def extract_link_from_url(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    urls = set()
    for a in soup.find_all('a'):
        href = urljoin(url, a.get('href'))
        if re.match(r"^(https://www\.kure-nct\.ac\.jp/).*(?!pdf)$", href):
            urls.add(href)

    return urls

def set_visited_urls(parent_url):
    url_list = set()
    url_list.add(parent_url)

    while(not len(url_list) == 0):
        url = url_list.pop()
        urls = extract_link_from_url(url)
        time.sleep(1)

        visited_urls.add(url)
        print(url)

        not_visited_urls = urls - visited_urls

        url_list = url_list | not_visited_urls

    return


parent_url = "https://www.kure-nct.ac.jp"
visited_urls = set()
set_visited_urls(parent_url)

print(visited_urls)

# wordlist = get_wordlist_from_QiitaURL(url)
# create_wordcloud(" ".join(wordlist))
