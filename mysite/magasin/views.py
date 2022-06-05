from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Categorie, Produit,Commande,Fournisseur
from django.core.paginator import Paginator

def index(request):
    template=loader.get_template('magasin/search.html')
    products=Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        products = Produit.objects.filter(libelle__icontains=item_name)
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return HttpResponse(template.render( { 'products':products} ))

def listnameCateg(request):
    template=loader.get_template('magasin/search.html')
    Categories=Categorie.objects.all()
    return HttpResponse(template.render( { 'Categories':Categories} ))

#fournisseur
def indexF(request):
    template=loader.get_template('magasin/mesFournisseurs.html')
    Fournisseurs=Fournisseur.objects.all()
    return HttpResponse(template.render( { 'Fournisseurs':Fournisseurs} ))

def listF(request):
    template=loader.get_template('magasin/mesFournisseurs.html')
    Fournisseurs=Fournisseur.objects.all()
    return HttpResponse(template.render( { 'Fournisseurs':Fournisseurs} ))


def list(request):
    template=loader.get_template('magasin/search.html')
    products=Produit.objects.all()
    return HttpResponse(template.render( { 'products':products} ))
# Create your views here.

def detail(request, myid):
    template=loader.get_template('magasin/detail.html')
    products = Produit.objects.get(id=myid)
    return  HttpResponse(template.render( {'product': products}) )




def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()
        return redirect('confirmation')
    return render(request, 'magasin/checkout.html') 

def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    template=loader.get_template('magasin/confirmation.html')
    return HttpResponse(template.render( {'name': nom} )) 
