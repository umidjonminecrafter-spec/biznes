from django.urls import path
from .views import index,category,single,contact,detail,NewsCreateView,NewsUpdateView,NewsDeleteView,news_detail,search_news,categoriya

urlpatterns = [
path('',index, name='index'),
path('category/',category, name='category'),
path('categoriya/<slug:slug>/',categoriya, name='categoriya'),

    path('contact/',contact, name='contact'),
    path('single/',single, name='single'),
path('detail/<slug:slug>/', detail, name='detail'),
    path('news-create/', NewsCreateView.as_view(), name='news-create'),
    path('news-update/<int:pk>/', NewsUpdateView.as_view(), name='news-update'),
    path('news-delete/<int:pk>/', NewsDeleteView.as_view(), name='news-delete'),
# blog/urls.py
    path('news/<int:pk>/', news_detail, name='news_detail'),
path('search/',search_news, name='search'),




]