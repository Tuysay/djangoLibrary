from django.urls import path, re_path
from . import views
# from django.conf.urls import url




urlpatterns = [
     path('', views.index, name='index'),
     re_path('', views.index, name='index'),
]
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
# ]
