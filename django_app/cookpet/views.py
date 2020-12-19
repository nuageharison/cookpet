from django.shortcuts import render, redirect
from datetime import datetime
from .models import Pet
from .forms import PetForm
from .models import Meal
from .models import MealPlan
from .forms import MealForm
from .models import User
from .models import UserPet
from .models import Photo
from .forms import LoginForm
from .forms import MealsForm2
from .forms import TestForm
from .forms import PetSelectForm
from django.utils import timezone


from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.contrib.auth.decorators import login_required

class cookpet:
    p_id=0
    u_id=0
    up_id=0
    new_user=0
def menu(request):
    return render(request, 'cookpet/menu.html')
def daietto(request):
    return render(request, 'cookpet/daietto.html')
def day1(request):
    return render(request, 'cookpet/day1.html')
def day2(request):
    return render(request, 'cookpet/day2.html')
def day3(request):
    return render(request, 'cookpet/day3.html')
def eat(request):
    return render(request, 'cookpet/eat.html')


def afeat(request):
    params = {
        'shinka': [],
        'message':'おいしい！',

    }
    upid = UserPet.objects.get(id=cookpet.up_id)
    p = Pet.objects.get(id=cookpet.p_id)
    point=upid.point
    if((point>10)and(p.advid>0)):
        UserPet.objects.filter(id=upid.id).update(PetId=p.advid)
        upid = UserPet.objects.get(id=cookpet.up_id)
        UserPet.objects.filter(id=upid.id).update(point=0)
        UserPet.objects.update()
        cookpet.p_id=upid.PetId
        params['message']='進化！'
    pid=Pet.objects.get(id=upid.PetId)
    params['shinka']=[pid]
    return render(request, 'cookpet/afeat.html',params)
def login(request):
    params = {
        'main': [],
        'form': LoginForm(),
        'meal':[],

    }
    if (request.method == 'POST'):
        num = request.POST.get('id')
        pas = request.POST.get('pas')
        uid = User.objects.get(name=num)
        cookpet.u_id=uid.id
        upid=UserPet.objects.get(UserId=uid.id)
        cookpet.up_id=upid.id
        item=Pet.objects.get(id=upid.PetId)
        cookpet.p_id=item.id
        params['main'] = [item]
        params['form'] = LoginForm(request.POST)
        return render(request, 'cookpet/index.html', params)
    return render(request, 'cookpet/login.html',params)

def index(request):
    params={
        'main':[],
    }
    item = Pet.objects.get(id=cookpet.p_id)
    params['main'] = [item]
    return render(request, 'cookpet/index.html',params)


def test(request):
    params = {
        'form' : TestForm(),
        'obj' : [],
        'pet': [],
    }
    pet = Pet.objects.get(id=cookpet.p_id)
    params['pet'] = [pet]
    if request.method == 'POST':
        params['form'] = TestForm(request.POST, request.FILES)
        if params['form'].is_valid():
            params['form'].save()
            ph= Photo.objects.last()
            num1 = request.POST.get('choice')
            meal = Meal.objects.get(id=num1)
            upid = cookpet.up_id
            Photo.objects.filter(id=ph.id).update(UserPetId=upid)
            Photo.objects.filter(id=ph.id).update(name=meal.name)
            ph = Photo.objects.last()
            params['obj']=[ph]
            upid = cookpet.up_id
            userpet = UserPet.objects.get(id=upid)
            UserPet.objects.filter(id=upid).update(point=userpet.point + meal.star)

            nowtime = timezone.now()
            UserPet.objects.filter(id=upid).update(lasttime=nowtime)

            print(nowtime)
        return render(request, 'cookpet/eat.html', params)
    return render(request, 'cookpet/test.html',params)


def touroku(request):
    ps=[]
    for obj in Pet.objects.all():
        if((obj.id==3)or(obj.id==6)or(obj.id==10)):
            ps.append(Pet.objects.get(id=obj.id))
    params = {
        'ps1':ps[0],
        'ps2':ps[1],
        'ps3':ps[2],

    }
    if (request.method == 'POST'):
        name = request.POST.get('id')
        pas = request.POST.get('pass')
        user=User(name=name,pas=pas)
        user.save()
        cookpet.new_user=User.objects.last()
        return render(request, 'cookpet/petSelect.html', params)
    return render(request, 'cookpet/touroku.html', params)


def ps1(request):
    user=cookpet.new_user.id
    pet=3
    userpet = UserPet(PetId=pet,UserId=user)
    userpet.save()
    return render(request, 'cookpet/login.html')
def ps2(request):
    user = cookpet.new_user.id
    pet = 6
    userpet = UserPet(PetId=pet, UserId=user)
    userpet.save()
    return render(request, 'cookpet/login.html')
def ps3(request):
    user = cookpet.new_user.id
    pet = 10
    userpet = UserPet(PetId=pet, UserId=user)
    userpet.save()
    return render(request, 'cookpet/login.html')