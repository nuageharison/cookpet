from django import forms
from .models import Meal
from .models import MealPlan
from .models import Photo
from .models import Pet
from django.contrib.auth import forms as auth_forms

class PetForm(forms.Form):
    id = forms.IntegerField(label='ID')
    file = forms.FileField()
class LoginForm(forms.Form):
    user = forms.CharField(max_length=50,label='USER')
    pas = forms.CharField(max_length=50,label='PASSWORD')

class MealForm(forms.Form):
    data = []
    for obj in Meal.objects.all():
        data.append([obj.id, obj.name + "★" * obj.star])
    choice = forms.ChoiceField(label='choice', choices=data, widget=forms.Select(attrs={'size': 1}))

    class Meta:
        model = Photo
        fields = ('img',)


class MealsForm2(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ( 'img',)


class TestForm(forms.ModelForm):
    data = []
    for obj in Meal.objects.all():
        data.append([obj.id, obj.name + "★" * obj.star])
    choice = forms.ChoiceField(label='料理を選ぼう！', choices=data, widget=forms.Select(attrs={'size': 1}))

    class Meta:
        model = Photo
        fields = ( 'img',)


class PetSelectForm(forms.Form):
    data = []
    for obj in Pet.objects.all():
        if((obj.id==3)or(obj.id==6)or(obj.id==8)):
            data.append([obj.id,obj.img])
    choice = forms.ChoiceField( choices=data, widget=forms.RadioSelect())

