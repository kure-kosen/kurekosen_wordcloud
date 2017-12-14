import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import time
import os

def create_wordcloud(text):
    # 環境に合わせてフォントのパスを指定する。
    fpath = "/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"

    # ストップワードの設定
    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して',
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て', 'に', 'を', 'は', 'の', 'が', 'と', 'た', 'し', 'で',
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', 'たち', 'いただき', 'ブック', '開く', '平成', '年度',
             '委員', '高専', 'KOUSEN', 'KUREKOUSEN', 'でき', 'なり', 'あり', '入学', '案内', '参加',
             'TOP', '最新', 'ページ', 'co', 'ba', '開催', '担当', '学生', '今回']

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

create_wordcloud(" ".join(wordlists))
