# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

OTDEL_CHOICES = (
    ('Прикладная Математика', 'Прикладная Математика'),
    ('Математика', 'Математика'),
    ('Биология', 'Биология'),

)


class Teacher(models.Model):
    class Meta:
        verbose_name_plural = 'Учителя деканата'
        verbose_name = 'Учителя деканата'

    name = models.CharField(max_length=255, blank=True)
    sirname = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=20)
    otdelenie = models.CharField(max_length=255, choices=OTDEL_CHOICES)
    position = models.CharField(max_length=255)
    biography = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class TeacherImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки учителей'
        verbose_name = 'Картинки Учителей'

    teacher = models.ForeignKey(Teacher)
    file = models.FileField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class LessonMath(models.Model):
    class Meta:
        verbose_name_plural = 'lessonMath'
        verbose_name = 'lesson'

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class LessonPm(models.Model):
    class Meta:
        verbose_name_plural = 'lessonPM'
        verbose_name = 'lesson'

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class LessonBiology(models.Model):
    class Meta:
        verbose_name_plural = 'lessonBiology'
        verbose_name = 'lesson'

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление новостей'
        verbose_name = 'Добавление новостей'

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    description = models.CharField(max_length=1000, verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст поста')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id


class NewsImage(models.Model):
    class Meta:
        verbose_name_plural = 'Картинки новостей'
        verbose_name = 'Картинки новостей'

    news = models.ForeignKey(News, verbose_name='выберите новость')
    image = models.ImageField(upload_to='', verbose_name='картинка')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)
