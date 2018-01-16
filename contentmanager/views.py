from django.shortcuts import render
from .models import New, Post, Author


def mainpage(request):
    context = {
        'news': New.objects.all(),
        'posts' : Post.objects.all(),
        'title': "главная",
    }
    return render(request, "home.html", context)

def laureates(request):
    context = {
        'title': "лауреаты",
        'laureates': Author.objects.all(),
    }
    return render(request, "laureates.html", context)
