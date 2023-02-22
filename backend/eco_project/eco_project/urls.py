from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mission/', include("Mission.urls")),
    path('member/', include("member.urls")),
    path('mileage/', include("mileage.urls")),
    path('news/', include("news.urls")),
]