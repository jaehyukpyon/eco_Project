from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup

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
