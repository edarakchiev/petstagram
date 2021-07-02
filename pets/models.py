from django.db import models


class Pet(models.Model):
    CAT_CHOICE = 'Cat'
    DOG_CHOICE = 'Dog'
    PARROT_CHOICE = 'Parrot'
    ALL_CHOICES = (
        (CAT_CHOICE, 'cat'),
        (DOG_CHOICE, 'dog'),
        (PARROT_CHOICE, 'parrot'),
    )
    type = models.CharField(
        choices=ALL_CHOICES,
        max_length=6,
    )
    name = models.CharField(
        max_length=6
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
