from django.shortcuts import render

from .models import Article

def article_list(request):
    art = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html',{'art':art})