# Generated by Django 5.0.3 on 2024-04-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_trending',
            field=models.BooleanField(default=False),
        ),
    ]
