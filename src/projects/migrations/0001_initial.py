# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 20:58
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(upload_to='actors/logo')),
                ('address', models.TextField()),
                ('geo', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('website', models.URLField()),
                ('description', models.TextField()),
                ('convention', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Acteur',
            },
        ),
        migrations.CreateModel(
            name='ActorKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Mot-clef acteur',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(upload_to='events/feature-image')),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('deadline_date', models.DateField()),
                ('featured', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ev\xe9nement',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(blank=True, max_length=255)),
                ('featured_image', models.ImageField(upload_to='experiences/feature-image')),
                ('zip_code', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('fulfilled', models.BooleanField()),
                ('featured', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('contacts', models.ManyToManyField(to='projects.Contact')),
            ],
            options={
                'verbose_name': 'Exp\xe9rience',
            },
        ),
        migrations.CreateModel(
            name='ExperienceKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Mot-clef exp\xe9rience',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images')),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='participants/logo')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Participant',
            },
        ),
        migrations.AddField(
            model_name='experience',
            name='images',
            field=models.ManyToManyField(to='projects.Image'),
        ),
        migrations.AddField(
            model_name='experience',
            name='keywords',
            field=models.ManyToManyField(to='projects.ExperienceKeyword'),
        ),
        migrations.AddField(
            model_name='experience',
            name='participants',
            field=models.ManyToManyField(to='projects.Participant'),
        ),
        migrations.AddField(
            model_name='actor',
            name='contacts',
            field=models.ManyToManyField(to='projects.Contact'),
        ),
        migrations.AddField(
            model_name='actor',
            name='images',
            field=models.ManyToManyField(to='projects.Image'),
        ),
        migrations.AddField(
            model_name='actor',
            name='keywords',
            field=models.ManyToManyField(to='projects.ActorKeyword'),
        ),
    ]
