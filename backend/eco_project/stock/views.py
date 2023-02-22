from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .serializers import StockPriceSerializer

@api_view(['GET'])
def stock_autocomplete(request):
    if request.method == 'GET':
        search_text = request.GET.get('text', '')
        url = 'http://www.sedaily.com/Stock/Quote/JsonSearchData'
        params = {'text': search_text}
        response = requests.get(url, params=params)
        data = response.json()
        current_price = float(data['Items'][0]['CurrentPrice'].replace(',', '')) # Extract CurrentPrice value and convert to float
        serializer = StockPriceSerializer({'current_price': current_price})
        return Response(serializer.data)