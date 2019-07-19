from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def greet(request):
    return HttpResponse("<H1> Hello PNV softtech!!!</H1>")

def get_one_article(request):
    obj=Article.objects.first()
    context ={'art':obj}
    return render(request,'frontpage.html',context)




def get_all_article(request):
    objs=Article.objects.all()

    context={'all_articles':objs}
    return render(request,'all.html',context)  