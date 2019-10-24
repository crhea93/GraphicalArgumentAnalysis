from django.conf.urls import url
from django.urls import path

from link import views

urlpatterns = [
    path('add_link', views.add_link, name='add_link'),
    path('delete_link', views.delete_link, name='delete_link'),
    path('update_link', views.update_link, name='update_link')
]