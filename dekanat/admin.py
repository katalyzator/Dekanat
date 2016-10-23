from django.contrib import admin

# Register your models here.

from .models import Teacher, TeacherImage, LessonPm, LessonBiology, LessonMath, News, NewsImage


class AdminTeacher(admin.ModelAdmin):
    class Meta:
        model = Teacher


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title']
    list_filter = ['title', 'timestamp']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = News


admin.site.register(News)

admin.site.register(NewsImage)

admin.site.register(Teacher, AdminTeacher)

admin.site.register(LessonPm)

admin.site.register(LessonMath)

admin.site.register(LessonBiology)
