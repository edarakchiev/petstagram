from django.shortcuts import render, redirect

from petstagram_2.common.models import Comment
from petstagram_2.pets.forms import PetCreateForm
from petstagram_2.pets.models import Pet, Like


def all_pets(request):
    context = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk)
    context = {
        'pet': pet,
        'comment': comment,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(pet=pet_to_like)
    like.save()
    return redirect('details', pet_to_like.id)


def create(request):
    if request.method == 'POST':
        form = PetCreateForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            pet = Pet(
                type=type,
                name=name,
                age=age,
                image=image,
                description=description,
            )
            pet.save()
            return redirect('all pets')
    context = {
        'pets': Pet.objects.all(),
        'form': PetCreateForm(),
    }
    return render(request, 'pets/pet_create.html', context)
