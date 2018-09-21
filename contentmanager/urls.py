from django.conf.urls import url
from .views import mainpage, laureates, zhenya, post_detail, Researcher, post_detail
from apply.views import UploadView


urlpatterns = [
    url(r'^$', UploadView.as_view(), name = 'apply'),
    url(r'^laureates/', laureates, name='laureates'),
    url(r'^EvgeniyShurygin/', zhenya, name = 'zhenya'),
    url(r'^author/(?P<slug>[\w-]+)', Researcher.as_view(), name = 'author'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'detail'),
]
