from django.shortcuts import render
from django.http import HttpResponse
from ArticleApp.models import Article
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    output = Article.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'output': output,
    })
    return HttpResponse(template.render(context))

def details(request,art_id):
    template = loader.get_template('details.html')
    output = Article.objects.get(pk=art_id)
    context = RequestContext(request, {
        'output': output,
    })
    return HttpResponse(template.render(context))
    
