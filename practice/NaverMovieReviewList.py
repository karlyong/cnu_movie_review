# 네이버 영화에서 영화를 선택하고
#영화리뷰 점수 작성자 날짜 정보를 수집하는 코드

import pprint
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=2'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
reveiw_list = doc.select('div.score_result > ul > li')

for i,one in enumerate(reveiw_list):
    print('#####################')
    #review score 수집
    score = one.select('div.star_score>em')[0].get_text()
    #reveiw content t수집
    #관람객 키워드 0 len =2 [관람객, 리뷰정보]
    #관람객 키워드 x len= 1 [리뷰정보]
    review_select = one.select('div.score_reple >p > span')[-1].get_text().strip() #strip 함수 공백제거

    # if len (review_select)==2:
    #     review=review_select[1].get_text()
    # elif len (review_selcet)==1:
    #     review = review_select[0].get_text()
    # j = 0
    # if len(review_select) == 2:
    #     j = 1
    # review = review_select[j].get_text()

    print('SCORE==> {}'.format(score))
    print('REVIwE==>{}'.format(review_select))

