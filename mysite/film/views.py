from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Categorie,Film,Realisateur
from django.core.paginator import Paginator

def indexx(request):
    template=loader.get_template('film/search.html')
    films=Film.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        films = Film.objects.filter(libelle__icontains=item_name)
    paginator = Paginator(films, 8)
    page = request.GET.get('page')
    films = paginator.get_page(page)
    return HttpResponse(template.render( { 'films':films} ))

def liste(request):
    template=loader.get_template('film/search.html')
    films=Film.objects.all()
    return HttpResponse(template.render( { 'films':films} ))
# Create your views here.

def detail(request, myid):
    template=loader.get_template('film/detail.html')
    films = Film.objects.get(id=myid)
    return  HttpResponse(template.render( {'films': films}) )

#fournisseur
def indexR(request):
    template=loader.get_template('film/mesRealisateurs.html')
    Realisateurs=Realisateur.objects.all()
    return HttpResponse(template.render( { 'Realisateurs':Realisateurs} ))

def listR(request):
    template=loader.get_template('film/mesRealisateurs.html')
    Realisateurs=Realisateur.objects.all()
    return HttpResponse(template.render( { 'Realisateurs':Realisateurs} ))
