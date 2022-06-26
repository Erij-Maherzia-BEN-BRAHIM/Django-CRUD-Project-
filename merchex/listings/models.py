from django.utils import timezone
from django.db import models
from django.urls import reverse

from merchex.settings import AUTH_USER_MODEL

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    tel=models.IntegerField()
    ville=models.CharField(max_length=100)
    gerant=models.CharField(max_length=50)
    def __str__(self) :
        return f'{self.nom}'

class Product(models.Model):
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
    name=models.CharField(max_length=100,choices=MARQUES)
    slug=models.SlugField(max_length=100)
    image=models.ImageField(upload_to='static/',blank=True , null=True)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE)
    def __str__(self) :
            return f'{self.name}'
    def get_absolute_url(self):
        return reverse("product",kwargs={"slug":self.slug})
    def etat_de_stock(self):
        if self.stock>0:
            return "en stock"
        else:
            return "hors stock"
class Order(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)
    ordered_date= models.DateTimeField(blank=True, null=True)
    def __str__(self):
         return f'{self.product.name}({self.quantity})'
    def get_total(self):
        total=self.quantity * self.product.price
        return total
           
class Cart(models.Model):
    user=models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders=models.ManyToManyField(Order)
    total_orders=models.FloatField(default=0.0)
    def __str__(self):
         return self.user.username

    def get_total_cart(self):
        for o in total_orders:
            total_orders=sum(o.orders.get_total())
            total_orders.save()
        return total_orders


    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered=True
            order.oredered_date= timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)
