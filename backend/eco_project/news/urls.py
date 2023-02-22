from django.urls import path
from .views import InnerTextView

urlpatterns = [
    path('inner_text/', InnerTextView.as_view(), name='inner_text'),
]
