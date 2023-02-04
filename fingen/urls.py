from django.urls import path, include
from fingen.views import home

app_name = 'fingen'

urlpatterns = [
    path('', home, name="home")
]