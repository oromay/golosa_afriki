from django.core.mail import send_mail
from django.shortcuts import render,  get_object_or_404
from django.views.generic import TemplateView
from ga.settings.base import EMAIL_HOST_USER
from .models import New, Post, Author
from .forms import ContactUsForm


def mainpage(request):
    queryset = Post.objects.all().order_by("-timestamp")
    form = ContactUsForm(request.POST or None)
    context = {
        'form':form,
        'news': New.objects.all(),
        'posts' : queryset,
        'title': "Голоса Африки",
        'contact_name': False,
    }
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        name = form.cleaned_data['first_name']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['moreplavatel@gmail.com',]
        message = 'Сообщение от %s \n %s \n via %s' %(name, message, sender)
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, EMAIL_HOST_USER, recipients, fail_silently=False)
        context['contact_name'] = name
    return render(request, "home.html", context)


def post_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = ContactUsForm(request.POST or None)
    context = {
        'form':form,
        'instance': instance,
        'title' : "ГА: " + instance.title
    }
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        name = form.cleaned_data['first_name']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['moreplavatel@gmail.com',]
        message = 'Сообщение от %s \n %s \n via %s' %(name, message, sender)
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, EMAIL_HOST_USER, recipients, fail_silently=False)
        context['contact_name'] = name
    return render(request, "post_detail.html", context)



def laureates(request):
    form = ContactUsForm(request.POST or None)
    context = {
        'form':form,
        'title': "Лауреаты",
        'laureates': Author.objects.all(),
    }
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        name = form.cleaned_data['first_name']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['moreplavatel@gmail.com',]
        message = 'Сообщение от %s \n %s \n via %s' %(name, message, sender)
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, EMAIL_HOST_USER, recipients, fail_silently=False)
        context['contact_name'] = name
    return render(request, "laureates.html", context)


def zhenya(request):
    form = ContactUsForm(request.POST or None)
    context = {
        'form':form,
        'title': "Евгений Шурыгин",
    }
    if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['first_name']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['moreplavatel@gmail.com',]
            message = 'Сообщение от %s \n %s \n via %s' %(name, message, sender)
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, EMAIL_HOST_USER, recipients, fail_silently=False)
            context['contact_name'] = name
    return render(request, "zhenya.html", context)


class Researcher(TemplateView):
    template_name = 'author.html'
    def get_context_data(self, ** kwargs):
        context = super(Researcher, self).get_context_data( ** kwargs)
        return context
