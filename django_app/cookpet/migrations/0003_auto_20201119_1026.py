# Generated by Django 3.1.1 on 2020-11-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookpet', '0002_auto_20201119_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Hello',
        ),
    ]
