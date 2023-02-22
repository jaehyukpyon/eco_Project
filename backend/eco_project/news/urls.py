from django.urls import path
from .views import InnerTextView, NewsView

urlpatterns = [
    path('', NewsView.as_view()),
    path('inner_text/', InnerTextView.as_view(), name='inner_text'),
]
