# Generated by Django 4.0.4 on 2022-05-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_fournisseur_produitc_commande_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='address',
            field=models.CharField(default='tunis', max_length=200),
        ),
        migrations.AddField(
            model_name='commande',
            name='email',
            field=models.EmailField(default='anonymous@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='commande',
            name='items',
            field=models.CharField(default='xxx', max_length=300),
        ),
        migrations.AddField(
            model_name='commande',
            name='nom',
            field=models.CharField(default='Hatem', max_length=150),
        ),
        migrations.AddField(
            model_name='commande',
            name='pays',
            field=models.CharField(default='tunisie', max_length=300),
        ),
        migrations.AddField(
            model_name='commande',
            name='ville',
            field=models.CharField(default='La Marsa', max_length=200),
        ),
        migrations.AddField(
            model_name='commande',
            name='zipcode',
            field=models.CharField(default='1234', max_length=300),
        ),
    ]