from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get$', views.index, name='index'),
    url(r'^create', views.create, name='create'),
    url(r'^apply', views.apply, name='apply')
]