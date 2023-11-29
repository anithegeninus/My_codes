
from django.urls import re_path,path
from . import views

app_name = 'articles' 

urlpatterns = [
    re_path(r'^$', views.article_list,name="list"),
   
]