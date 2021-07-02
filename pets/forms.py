from django import forms

from petstagram_2.pets.models import Pet


class PetCreateForm(forms.Form):
    type = forms.ChoiceField(
        choices=(
            ('Cat', 'cat'),
            ('Dog', 'dog'),
            ('Parrot', 'parrot'),
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
            }
        )
    )
    image = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2'
            }
        )
    )
