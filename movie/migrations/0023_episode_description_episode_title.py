# Generated by Django 5.0.3 on 2024-05-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0022_remove_episode_name_remove_season_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
