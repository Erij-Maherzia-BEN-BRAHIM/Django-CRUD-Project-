
from django.shortcuts import redirect, render, get_object_or_404
from listings.forms import ContactUsForm, FournisseurForm, ProduitForm
from listings.models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


@login_required
def welcome(request):
    return render(request,'listings/welcome.html')
@login_required
def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request,'listings/fournisseur_list.html',{'fournisseurs':fournisseurs})
@login_required
def fournisseur_detail(request,id):
    fournisseur= Fournisseur.objects.get(id=id)
    return render(request, 'listings/fournisseur_detail.html',{'fournisseur':fournisseur})

@login_required
def produit_list(request):
    products= Product.objects.all()
    return render(request, 'listings/produit_list.html', {'products':products})
@login_required
def produit_detail(request,slug):
    product=get_object_or_404(Product, slug=slug)
    return render(request, 'listings/produit_detail.html',context={"product":product})

@login_required    
def aPropos(request):
    return render(request, 'listings/a_propos.html' )

@login_required
def fournisseur_create(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save()
            return redirect('fournisseur-detail', fournisseur.id)
    else:
        form = FournisseurForm()
    return render(request, 'listings/fournisseur_create.html',  {'form': form})

""" @login_required
def produit_create(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            produit = form.save()
            return redirect('produit-detail', produit.slug)

    else:
        form = ProduitForm()

    return render(request,
            'listings/produit_create.html', {'form': form})
 """
""" @login_required
def produit_update(request, id):
    produit= Product.objects.get(id=id)

    if request.method =='POST':
        form = ProduitForm(request.POST , instance=produit) #on pré-remplir le formulaire avec un pdt existant   
        if form.is_valid():
            form.save()

            return redirect('produit-detail', produit.id)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'listings/produit_update.html', {'form': form})
 """
@login_required
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

@login_required
def produit_delete(request,slug):
    product= Product.objects.get(slug=slug)
    if request.method=='POST':
        product.delete()
        return redirect('produit-list')
    return render(request, 'listings/produit_delete.html', {'product': product})

@login_required
def fournisseur_delete(request,id):
    fournisseur= Fournisseur.objects.get(id=id)
    if request.method=='POST':
        fournisseur.delete()
        return redirect('fournisseur-list')
    return render(request, 'listings/fournisseur_delete.html', {'fournisseur': fournisseur})

@login_required
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

def checkout(request):
    return render(request, 'listings/checkout.html')

def add_to_cart(request, slug):
    user=request.user
    product=get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order , created=Order.objects.get_or_create(user=user,ordered=False, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity+=1
        order.save()
    return  redirect(reverse("product", kwargs={"slug":slug})) 
def cart(request):
    cart=get_object_or_404(Cart,user=request.user)
    return render(request, 'listings/cart.html', context={"orders":cart.orders.all()})
def cart_delete(request):
    cart=request.user.cart
    if cart:
        cart.delete()
    return redirect('welcome')

def etat_de_stock(request):
    if Product.stock>0:
        etat="en stock"
    else: etat="hors stock"
    return render(request, context={"etat": etat})