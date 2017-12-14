import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import time
import os

def create_wordcloud(text):
    # 環境に合わせてフォントのパスを指定する。
    #fpath = "/System/Library/Fonts/HelveticaNeue-UltraLight.otf"
    fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

    # ストップワードの設定
    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して',
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て', 'に', 'を', 'は', 'の', 'が', 'と', 'た', 'し', 'で',
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', 'ブック', '開く', '平成', '年度',
             '委員']

    wordcloud = WordCloud(background_color="white",font_path=fpath, width=900, height=500, stopwords=set(stop_words)).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

files = os.listdir('wordlist/')
wordlists = []
for file in files:
    print(file)
    if file == ".DS_Store":
        continue

    with open("wordlist/" + file, "r") as f:
        line = f.readline().replace("\n", "")
        wordlists.append(line)

# wordlist = get_wordlist_from_QiitaURL("https://www.kure-nct.ac.jp/")
# print(wordlist)
create_wordcloud(" ".join(wordlists))
