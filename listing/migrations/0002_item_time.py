# Generated by Django 2.0.5 on 2018-05-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]