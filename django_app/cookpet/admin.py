from django.contrib import admin
from .models import Pet
from .models import User
from .models import UserPet
from .models import Document
from .models import Friend
from .models import Meal
from .models import MealPlan
from .models import Photo


# Register your models here.
admin.site.register(Pet)
admin.site.register(User)
admin.site.register(UserPet)
admin.site.register(Friend)
admin.site.register(Document)
admin.site.register(Meal)
admin.site.register(MealPlan)
admin.site.register(Photo)
