from django.contrib import admin
from listings.models import Fournisseur , Produit
# Register your models here.

#admin.site.register(Listing)

class FournisseurAdmin(admin.ModelAdmin):
    list_display= ('nom','tel','ville')
admin.site.register(Fournisseur, FournisseurAdmin)

class ProduitAdmin(admin.ModelAdmin):
    list_display= ('nomProduit','quantiteEnStock')
admin.site.register(Produit, ProduitAdmin)