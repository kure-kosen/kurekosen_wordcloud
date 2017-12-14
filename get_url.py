import re
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests

def extract_link_from_url(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "lxml")

    urls = set()
    for a in soup.find_all('a'):
        href = urljoin(url, a.get('href'))
        # 呉高専のドメインのhtmlファイルのみ収集する
        if re.match(r"^(https://www\.kure-nct\.ac\.jp/).*(\.html)$", href):
            urls.add(href)

    return urls


def main():
	visited_urls = set()

	url_list = set()

	url_list.add("https://www.kure-nct.ac.jp/")

	# IWだけaタグのリンク先でredirectさせててアクセスできてなかったので追加
	url_list.add("https://www.kure-nct.ac.jp/incubation/H29_top/index.html")

	while(not len(url_list) == 0):
	    url = url_list.pop()
	    urls = extract_link_from_url(url)
	    time.sleep(1)

	    visited_urls.add(url)
	    print(url)

	    not_visited_urls = urls - visited_urls

	    url_list = url_list | not_visited_urls

	with open("url.txt", "w") as file:
	    file.writelines("\n".join(visited_urls))

if __name__ == '__main__':
	main()
