from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Author, Article
# Create your views here.

def show_all(request):
    list = Article.objects.all()
    template = loader.get_template("show.html")
    context = {
    "list" : list,
    }
    return HttpResponse(template.render(context, request))
