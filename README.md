# kurekosen_wordcloud
呉高専HPをスクレイピングしてワードクラウドを作った

# Usage

1. `python get_url.py`  
Generate `url.txt` including accessible url of Kurekosen.

2. `python get_wordlist.py`  
Generate `wordlist/#{url}.txt` separated by word the content of the website.

3. `python wordcloud.py`  
Create word cloud image.
