from django.http import Http404
from django.shortcuts import render

from .models import LessonBiology, LessonMath, LessonPm

from .models import News, NewsImage


# Create your views here.

def home_view(request):
    context = {}
    template = 'dekanat/index.html'

    return render(request, template, context)


def pm_view(request):
    pm = LessonPm.objects.all()
    context = {'lesson': pm}
    template = 'pm.html'

    return render(request, template, context)


def math_view(request):
    math = LessonMath.objects.all()
    context = {'lesson': math}
    template = 'math.html'

    return render(request, template, context)


def biology_view(request):
    biology = LessonBiology.objects.all()
    context = {'lesson': biology}
    template = 'biology.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)


def single(request, id):
    try:
        news = News.objects.get(id=id)

        images = NewsImage.objects.filter(news=news)

        context = {"news": news, "images": images}
        template = 'single_post.html'

        return render(request, template, context)

    except News.DoesNotExist:
        raise Http404
    except NewsImage.DoesNotExist:
        raise Http404


def news_view(request):
    news = News.objects.all().order_by('-timestamp')
    context = {"news": news}
    template = 'news.html'

    return render(request, template, context)
