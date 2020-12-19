from django.db import models

class Document(models.Model):
    photo = models.ImageField(upload_to='documents/', default='defo')
