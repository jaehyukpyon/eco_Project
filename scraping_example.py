import requests
from bs4 import BeautifulSoup

inner_text_list = []
# send a GET request to the URL
for i in range(1,3):
    url = f"https://www.k-re100.or.kr/bbs/board.php?bo_table=sub2_2_1&page={i}"
    response = requests.get(url)

    # parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all li elements inside div.bo_list
    li_elements = soup.select('div.bo_list ul li')

    # extract the innerText of each li element and split it based on the relevant HTML tags
    for li in li_elements:
        span_elements = li.select('span')
        span_texts = [span.get_text(strip=True) for span in span_elements]
        inner_text_list.append(span_texts)
    
    # print the innerText array
print(inner_text_list)
