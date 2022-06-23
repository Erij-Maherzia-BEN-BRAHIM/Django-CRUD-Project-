from django.db import models

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    tel=models.IntegerField(default=0)
    ville=models.CharField(max_length=100)
    gerant=models.CharField(max_length=50)
    def __str__(self) :
        return f'{self.nom}'

class Produit(models.Model):
    FOURREE="FR"
    CHOCOTOM="CH"
    SMILE="SM"
    SAIDA="SA"
    BINTO="BI"
    MARQUES=[
    (FOURREE,"Fourree"),
    (CHOCOTOM,"Chocotom"),
    (SMILE,"Smile"),
    (SAIDA,"Saida"),
    (BINTO,"Binto")
    ]
    nomProduit=models.CharField(max_length=100,choices=MARQUES)
    image=models.ImageField(upload_to='static/',blank=True)
    prixAchat=models.FloatField(default=0)
    prixVente=models.FloatField(default=0)
    quantiteEnStock=models.IntegerField(default=0)
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE)
    def __str__(self) :
            return f'{self.nomProduit} '
