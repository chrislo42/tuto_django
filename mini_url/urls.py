from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^url/$', views.miniurl_list, name='miniurl_list'),
    url(r'^url/new/$', views.miniurl_edit, name='miniurl_edit'),
    url(r'^(?P<code>.+)/$', views.miniurl_redir, name='miniurl_redir'),
    url(r'^url/edit/(?P<pk>\d)$', views.URLUpdate.as_view(), name='url_update'),
    url(r'^url/del/(?P<pk>\d)$', views.URLDelete.as_view(), name='url_delete'),
]