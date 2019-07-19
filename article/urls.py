from django.urls import path
from .views import greet,get_one_article,get_all_article
urlpatterns=[
    path('hello/',greet),
    path('first/',get_one_article),
    path('all/',get_all_article),
]