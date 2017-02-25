from django.conf.urls import url , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    url(r'^$', views.Main),
    url(r'^all/$', views.Dishes),
    url(r'^add/$', views.Add),
    url(r'^del/(\d+)/$', views.Delete, name='main'),
    url(r'^dishes/(\d+)/$', views.Dishes_id, name = 'main'),
    url(r'^garnish/$', views.Garnish, name = 'main'),


]
