from django.urls import path
from concepts import views
urlpatterns = [
    path('delete_block', views.delete_block, name='delete_block'),
    path('add_block', views.add_block, name='add_block'),
    path('update_block',views.update_block, name='update_block'),
    path('delete_block',views.delete_block, name='delete_block'),
    path('drag_function',views.drag_function, name='drag_function')
]