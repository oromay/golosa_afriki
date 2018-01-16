from django.conf.urls import url
from .views import mainpage, laureates
from apply.views import UploadView


urlpatterns = [
    url(r'^$', mainpage, name='home'),
    url(r'^laureates/', laureates, name='laureates'),
    url(r'^apply/', UploadView.as_view(), name = 'apply'),
    url(r'^author/(?P<slug>[\w-]+)', UploadView.as_view(), name = 'author'),
]
