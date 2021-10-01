from django.urls import path

from .views import scraping_home

app_name = 'scraping'

urlpatterns = [
    path('', scraping_home, name='home'),

]
