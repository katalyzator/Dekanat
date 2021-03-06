# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-17 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonBiology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('credit', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessonBiology',
            },
        ),
        migrations.CreateModel(
            name='LessonMath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('credit', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessonMath',
            },
        ),
        migrations.CreateModel(
            name='LessonPm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('credit', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lessonPM',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('sirname', models.CharField(blank=True, max_length=255)),
                ('age', models.IntegerField(default=20)),
                ('otdelenie', models.CharField(choices=[('\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430', '\u041f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u0430\u044f \u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430'), ('\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430', '\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430'), ('\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f', '\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f')], max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0423\u0447\u0438\u0442\u0435\u043b\u044f \u0434\u0435\u043a\u0430\u043d\u0430\u0442\u0430',
                'verbose_name_plural': '\u0423\u0447\u0438\u0442\u0435\u043b\u044f \u0434\u0435\u043a\u0430\u043d\u0430\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='TeacherImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dekanat.Teacher')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0423\u0447\u0438\u0442\u0435\u043b\u0435\u0439',
                'verbose_name_plural': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0443\u0447\u0438\u0442\u0435\u043b\u0435\u0439',
            },
        ),
    ]
