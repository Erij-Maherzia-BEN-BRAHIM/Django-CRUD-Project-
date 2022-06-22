from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.forms import ContactUsForm, FournisseurForm, ProduitForm
from listings.models import Fournisseur, Produit
from django.core.mail import send_mail

def index(request):
    return render(request,'listings/index.html')
def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request,'listings/fournisseur_list.html',{'fournisseurs':fournisseurs})

def fournisseur_detail(request,id):
    fournisseur= Fournisseur.objects.get(id=id)
    return render(request, 'listings/fournisseur_detail.html',{'fournisseur':fournisseur})

def produit_list(request):
    produits= Produit.objects.all()
    return render(request, 'listings/produit_list.html', {'produits':produits})

def produit_detail(request,id):
    produit = Produit.objects.get(id=id)
    return render(request, 'listings/produit_detail.html',{'produit':produit})
def aPropos(request):
    return render(request, 'listings/a_propos.html' )
def fournisseur_create(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save()
            return redirect('fournisseur-detail', fournisseur.id)

    else:
        form = FournisseurForm()

    return render(request,
            'listings/fournisseur_create.html',
            {'form': form})

def produit_create(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save()
            return redirect('produit-detail', produit.id)

    else:
        form = ProduitForm()

    return render(request,
            'listings/produit_create.html',
            {'form': form})

def produit_update(request, id):
    produit= Produit.objects.get(id=id)

    if request.method =='POST':
        form = ProduitForm(request.POST , instance=produit) #on pré-remplir le formulaire avec un pdt existant   
        if form.is_valid():
            form.save()

            return redirect('produit-detail', produit.id)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'listings/produit_update.html', {'form': form})

def fournisseur_update(request, id):
    fournisseur = Fournisseur.objects.get(id=id)

    if request.method=='POST':
        form = FournisseurForm(request.POST, instance=fournisseur) #on pré-remplir le formulaire avec un pdt existant   
        if form.is_valid():
            form.save()

            return redirect('fournisseur-detail', fournisseur.id)
    else:
        form = FournisseurForm(instance=fournisseur)

    return render(request, 'listings/fournisseur_update.html', {'form': form})

def produit_delete(request,id):
    produit= Produit.objects.get(id=id)
    if request.method=='POST':
        produit.delete()
        return redirect('produit-list')
    return render(request, 'listings/produit_delete.html', {'produit': produit})

def fournisseur_delete(request,id):
    fournisseur= Fournisseur.objects.get(id=id)
    if request.method=='POST':
        fournisseur.delete()
        return redirect('fournisseur-list')
    return render(request, 'listings/fournisseur_delete.html', {'fournisseur': fournisseur})







def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via The Biscuit Factory Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['erijbb@gmail.com'],
        )
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
        return redirect('email-sent')
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
                'listings/contact.html',
                {'form': form})