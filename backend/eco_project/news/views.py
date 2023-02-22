from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# RE100 사이트를 GET
class InnerTextView(APIView):
    def get(self, request, format=None):
        inner_text_list = []
        for i in range(1, 3):
            url = f"https://www.k-re100.or.kr/bbs/board.php?bo_table=sub2_2_1&page={i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            li_elements = soup.select('div.bo_list ul li')
            for li in li_elements:
                span_elements = li.select('span')
                span_texts = [span.get_text(strip=True) for span in span_elements]
                inner_text_list.append(span_texts)
        return Response(inner_text_list, status=status.HTTP_200_OK)


# 최신 뉴스를 GET
class NewsView(APIView):
    def get(self, request):
  
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        url = "https://www.sedaily.com/Cube/CubeCollect/249"

        driver = webdriver.Chrome(options=options)  # Change this to the path of your chromedriver executable
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        collect_list = soup.select('#collectList > ul > li')[:10]

        news_result=[]
        for item in collect_list:
            result = []
            news_href = item.select_one('a')['href']
            thumb_img = item.select_one('.thumb span img')['src']
            text_title = item.select_one('.text_area h3').get_text(strip=True)
            text_sub = item.select_one('.text_sub').get_text(strip=True)
            result.append(news_href)
            result.append(thumb_img)
            result.append(text_title)
            result.append(text_sub)
            news_result.append(result)

        return Response(news_result, status=status.HTTP_200_OK)
