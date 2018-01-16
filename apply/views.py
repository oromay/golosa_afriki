from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from ipware.ip import get_real_ip
from .models import Apply, Attachment
from .forms import ApplyForm
from contentmanager.models import Elder
from contentmanager.utilities import days_left





# def applied_view(request):
#     lastappl = Apply.objects.last()
#     context = {
#         "name": lastappl.first_name,
#         "title": 'Спасибо!',
#     }
#     return render(request, "finished.html", context)


class UploadView(FormView):
    template_name = 'apply.html'
    form_class = ApplyForm
    success_url = '/'
    def get_context_data(self, ** kwargs):
        context = super(UploadView, self).get_context_data( ** kwargs)
        context['title'] = 'Голоса Африки'
        context['Elders'] = Elder.objects.all()
        context['days_left'] = days_left(2018,3,31, True)

        return context

    def form_valid(self, form):
        Apply.objects.create(first_name=form.cleaned_data['first_name'], second_name=form.cleaned_data['second_name'], email=form.cleaned_data['email'])
        lastappl = Apply.objects.last()
        for each in (form.cleaned_data['attachments']):
            Attachment.objects.create(document=each, applicant = lastappl)
        ip = get_real_ip(self.request)
        send_mail('новая заявка', '%s %s с ip %s отправил свою заявку - почта %s' % (lastappl.first_name, lastappl.second_name, ip, lastappl.email), settings.EMAIL_HOST_USER, ['moreplavatel@gmail.com',], fail_silently=False)
        return super(UploadView, self).form_valid(form)
