from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/cookpet/images/')
    advid = models.IntegerField()
    point = models.IntegerField()

    def __str__(self):
        return '<PetId=' + str(self.id) + ', ' + \
            self.name + '>'

class User(models.Model):
    name = models.CharField(max_length=100)
    pas = models.CharField(max_length=100)


    def __str__(self):
        return '<UserId=' + str(self.id) + ', ' + \
            self.name + '>'

class UserPet(models.Model):
    UserId = models.IntegerField()
    PetId = models.IntegerField()
    point = models.IntegerField(default=0)
    lasttime = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return '<UserPetId=' + str(self.id) + ', ' + \
            'UserId=' +str(self.UserId) + ', ' +'PetId=' + str(self.PetId) + '>'
# Create your models here.
class Document(models.Model):
    UserId = models.IntegerField()
    photo = models.ImageField(upload_to='documents/', default='defo')

class Friend(models.Model):
    name = models.CharField(max_length=100)
    point = models.IntegerField()

    def __str__(self):
        return '<PetId=' + str(self.id) + ', ' + \
            self.name + '>'


class Meal(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    planid = models.IntegerField()


    def __str__(self):
        return '<MealId=' + str(self.id) + ', ' + \
            self.name + '>'


class MealPlan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '<MealId=' + str(self.id) + ', ' + \
               self.name + '>'

class Photo(models.Model):
    name = models.CharField(default=0,max_length=100)
    UserPetId = models.IntegerField(default=0)
    img = models.ImageField(upload_to='media')
