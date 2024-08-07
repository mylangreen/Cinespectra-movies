# Generated by Django 5.0.3 on 2024-04-14 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img_url', models.URLField(max_length=250)),
                ('video_url', models.URLField(blank=True, max_length=250, null=True)),
                ('iframe_code', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('added_at', models.DateField(auto_now_add=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.category')),
            ],
        ),
    ]
