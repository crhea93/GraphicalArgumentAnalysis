from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('clear_CAM',views.clear_CAM, name='clear_CAM'),
    path('save_CAM', views.save_CAM, name='save_CAM'),
]
