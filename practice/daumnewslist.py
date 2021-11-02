# 다음 뉴스 목록을 for 문을 돌며 제목과 본문을 수집
import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
result = requests.get(url)
print(result)
doc = BeautifulSoup(result.text, 'html.parser')
url_list = doc.select ('ul.list_news2 a.link_txt')
for i, href in enumerate(url_list):
    new_url = href['href']
    # 기사 1건의 제목과 본문을 수집하는 코드
    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')  # parser로 읽는다
    contents = doc.select('section p')
    contents.pop(-1)  # 기자정보 삭제
    content = ''
    for info in contents:
        content += info.get_text()
    title = doc.select('h3.tit_view')[0].get_text()  # .==>class
    print('-----------------')
    print()
    print('title:{}'.format(title))
    print('content:{}'.format(content))


