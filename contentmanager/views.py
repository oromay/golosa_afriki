from django.shortcuts import render,  get_object_or_404
from .models import New, Post, Author


def mainpage(request):
    queryset = Post.objects.all().order_by("-timestamp")
    context = {
        'news': New.objects.all(),
        'posts' : queryset,
        'title': "главная",
    }
    return render(request, "home.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'instance': instance,
    }
    return render(request, "post_detail.html", context)



def laureates(request):
    context = {
        'title': "лауреаты",
        'laureates': Author.objects.all(),
    }
    return render(request, "laureates.html", context)


def zhenya(request):
    context = {
        'title': "Евгений Шурыгин",
    }
    return render(request, "zhenya.html", context)
