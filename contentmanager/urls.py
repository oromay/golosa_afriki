from django.conf.urls import url
from .views import mainpage, laureates, zhenya, post_detail
from apply.views import UploadView


urlpatterns = [
    url(r'^$', mainpage, name='home'),
    url(r'^laureates/', laureates, name='laureates'),
    url(r'^zhenya/', zhenya, name = 'apply'),
    url(r'^apply/', UploadView.as_view(), name = 'apply'),
    url(r'^author/(?P<slug>[\w-]+)', UploadView.as_view(), name = 'author'),
]
