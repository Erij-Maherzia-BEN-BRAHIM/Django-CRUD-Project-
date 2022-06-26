from django.contrib import admin
from listings.models import *
# Register your models here.

#admin.site.register(Listing)

class FournisseurAdmin(admin.ModelAdmin):
    list_display= ('nom','tel','ville')
admin.site.register(Fournisseur, FournisseurAdmin)

class ProduitAdmin(admin.ModelAdmin):
    list_display= ('name','price')
admin.site.register(Product, ProduitAdmin)


admin.site.register(Order)
admin.site.register(Cart)