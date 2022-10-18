from operator import index
from django.urls import path
from .views import *

urlpatterns = [
    path('', InicioView.as_view()),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    path('client/list/', ClientView.as_view(), name='client_list'),
]
