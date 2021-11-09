#네이버 영화 특정 코드를 입력하면 해당 영화의 리뷰를 수집하는 프로그램

import requests
from bs4 import  BeautifulSoup

#네이버 영화 코드
movie_code = '184311'

############
# 1. title 수집 #
############
title_url='https://movie.naver.com/movie/bi/mi/basic.naver?code={}'.format(movie_code)
result = requests.get(title_url)
doc = BeautifulSoup(result.text,'html.parser')

title = doc.select('h3.h_movie>a')[0].get_text()
print(title)
