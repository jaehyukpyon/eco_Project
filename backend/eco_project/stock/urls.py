from django.urls import path
from .views import stock_autocomplete

urlpatterns = [
    path('', stock_autocomplete, name='stock_autocomplete'),
]