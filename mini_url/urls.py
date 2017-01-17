from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^url/$', views.miniurl_list, name='miniurl_list'),
    url(r'^url/new/$', views.miniurl_edit, name='miniurl_edit'),
    url(r'^(?P<code>.+)/$', views.miniurl_redir, name='miniurl_redir')
]