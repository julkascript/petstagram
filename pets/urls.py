from django.urls import path

from pets.views import pets_index, pets_details, pets_likes, pets_create, pets_edit, pets_delete

urlpatterns = [
    path('', pets_index, name='pets index'),
    path('details/<int:pk>', pets_details, name='pets details'),
    path('like/<int:pk>', pets_likes, name='pets likes'),
    path('create/', pets_create, name='pets create'),
    path('edit/<int:pk>', pets_edit, name='pets edit'),
    path('delete/<int:pk>', pets_delete, name='pets delete'),
]