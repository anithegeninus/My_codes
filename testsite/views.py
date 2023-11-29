from django.shortcuts import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('about')
   return render(request, 'about.html')
   
def ContactUs(request):
   #return render(request, 'about.html')
    return HttpResponse('ContactUs')
