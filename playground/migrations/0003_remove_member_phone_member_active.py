# Generated by Django 4.2.2 on 2023-06-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_member_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
