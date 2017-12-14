import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import requests
import MeCab as mc
import re
import time
from urllib.parse import urljoin

def create_wordcloud(text):
    # 環境に合わせてフォントのパスを指定する。
    #fpath = "/System/Library/Fonts/HelveticaNeue-UltraLight.otf"
    fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

    # ストップワードの設定
    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して',
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て', 'に', 'を', 'は', 'の', 'が', 'と', 'た', 'し', 'で',
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, stopwords=set(stop_words)).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# wordlist = get_wordlist_from_QiitaURL("https://www.kure-nct.ac.jp/")
# print(wordlist)
# create_wordcloud(" ".join(wordlist))
