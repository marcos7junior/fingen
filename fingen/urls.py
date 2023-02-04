from django.urls import path, include
from fingen.views import home

urlpatterns = [
    path('', home, name="home")
]