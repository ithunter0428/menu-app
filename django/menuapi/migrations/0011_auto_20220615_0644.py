# Generated by Django 2.2 on 2022-06-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapi', '0010_auto_20220612_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='arrangeable',
        ),
        migrations.AddField(
            model_name='category',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]
