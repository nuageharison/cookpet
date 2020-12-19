# Generated by Django 3.1.1 on 2020-12-10 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookpet', '0013_remove_photo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='UserPetId',
            field=models.IntegerField(default=0),
        ),
    ]
