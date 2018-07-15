from django.shortcuts import render,  get_object_or_404
from django.views.generic import TemplateView
from .models import New, Post, Author


def mainpage(request):
    queryset = Post.objects.all().order_by("-timestamp")
    context = {
        'news': New.objects.all(),
        'posts' : queryset,
        'title': "главная",
    }
    return render(request, "home.html", context)


def post_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
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


class Researcher(TemplateView):
    template_name = 'author.html'
    def get_context_data(self, ** kwargs):
        context = super(Researcher, self).get_context_data( ** kwargs)
        return context
