from django.db import models

# Create your models here.
from email.policy import default
from django.db import models
from datetime import date
# Create your models here.
class Film(models.Model):
    TYPE_CHOICES=[('Enf','Enfant'),('Adu','Adulte'),('Tout','Tout le monde')]
    libelle=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=20,choices=TYPE_CHOICES,default='Tout')
    img=models.ImageField(blank=True)
    def __str__(self):
        return self.libelle
        #associations avec les autres classes
    categorie= models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    realisateur=models.ForeignKey('Realisateur', on_delete=models.CASCADE,null=True)
    
class Categorie(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()

    def __str__(self):
        return self.name 
        
class Realisateur(models.Model):
    nom=models.CharField(max_length=255)
    nationalite=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    
    def __str__(self):
        return self.nom+" "+self.nationalite

    from django.db import models

# Create your models here.
