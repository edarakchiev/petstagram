from django.urls import path

from petstagram_2.pets.views import all_pets, pet_details, pet_like, create

urlpatterns = [
    path('', all_pets, name='all pets'),
    path('details/<int:pk>', pet_details, name='details'),
    path('like/<int:pk>', pet_like, name='pet like'),
    path('create/', create, name='create')
]