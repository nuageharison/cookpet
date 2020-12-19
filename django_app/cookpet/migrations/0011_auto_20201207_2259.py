# Generated by Django 3.1.1 on 2020-12-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookpet', '0010_auto_20201207_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserPetId', models.IntegerField()),
                ('img', models.ImageField(upload_to='static/cookpet/images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='UserPetId',
        ),
        migrations.RemoveField(
            model_name='mealplan',
            name='img',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
