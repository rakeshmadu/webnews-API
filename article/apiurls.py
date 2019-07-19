from django.urls import path
from .news_api import  api_get_one_article, api_all_articles
from .news_api import api_get_article_id, api_get_articles_range, api_add_article

urlpatterns = [
    path('first/', api_get_one_article),
    path('all/', api_all_articles),
    path('<int:_id>/', api_get_article_id),
    path('<str:_range>/', api_get_articles_range),
    path('add', api_add_article),

]
