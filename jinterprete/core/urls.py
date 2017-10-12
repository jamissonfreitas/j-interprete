from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^image_to_string$', views.image_to_string, name='image_to_string'),
]