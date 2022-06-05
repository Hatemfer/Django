from email.policy import default
from django.db import models
from datetime import date
# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES=[('Enf','Enfant'),('Ad','Adulte'),('tout','Tout le monde')]
    libelle=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=200,choices=TYPE_CHOICES,default='tout')
    img=models.ImageField(blank=True)    
    def __str__(self):
        return self.libelle
        #associations avec les autres classes
    categorie= models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE,null=True)
    
class Categorie(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()

    def __str__(self):
        return self.name 
class Fournisseur(models.Model):
    nom=models.CharField(max_length=255)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    
    def __str__(self):
        return self.nom+" "+self.adresse

class ProduitC(Produit):
    duree_garantie=models.IntegerField()
    def __str__(self):
        return "Produit consommable"+str(self.duree_garantie)

class Commande(models.Model):
    items = models.CharField(max_length=300)
    pays = models.CharField(max_length=300)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=300)
    dateCde=models.DateField(null=True,default=date.today)
    total=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        
        return str(self.dateCde)+"\n"+str(self.produits)+"\n Total: "+str(self.total
        )
    from django.db import models

# Create your models here.
