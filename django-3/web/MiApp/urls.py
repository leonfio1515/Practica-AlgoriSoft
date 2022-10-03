from operator import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', InicioView.as_view()),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
]
