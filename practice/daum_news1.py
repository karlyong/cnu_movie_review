import requests
from bs4 import BeautifulSoup

# reuqest 라이브러리 사용해서 해당 url 코드 가져오기
url='https://news.v.daum.net/v/20211028092018253'
result= requests.get(url) # request로 소스를 가져와 result에 넣어놓는다
#print(result.text)

# soup 사용해서 원하는 정보 추출
doc= BeautifulSoup(result.text, 'html.parser')#parser로 읽는다
contents=doc.select('section p')
contents.pop(-1) #기자정보 삭제

content=''
for info in contents:
    content+= info.get_text()
#doc에 수프가 읽은 데이터가 들어있다.

# select 를 사용해서 데이터를 수집 무조건 리스트 타입으로 가져와야 한다
#html은 항상 태그 정보로 이루어져 있다.  f12 를 누르고 기사에 갖다 대면 태그가 나온다
#h3 중에서  class 가 tit view 인 tag를 가져오세요
title=doc.select('h3.tit_view')[0].get_text() #.==>class


print('-----------------')
print('title:{}'.format(title))
print('content:{}'.format(content))





