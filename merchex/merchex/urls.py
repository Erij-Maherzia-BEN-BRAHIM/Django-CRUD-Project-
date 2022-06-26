"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from listings.views import *
from django.contrib.auth.views import LoginView , LogoutView , PasswordChangeDoneView, PasswordChangeView
import authentification.views


urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentification/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentification/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentification/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('fournisseurs/', fournisseur_list , name='fournisseur-list'),
    path('fournisseurs/<int:id>/', fournisseur_detail, name='fournisseur-detail'),
    path('fournisseurs/<int:id>/update/', fournisseur_update, name='fournisseur-update'),
    path('fournisseurs/<int:id>/delete/', fournisseur_delete, name='fournisseur-delete'),
    path('fournisseurs/add/', fournisseur_create , name='fournisseur-create'),
    path('product/', produit_list, name='product-list'),
    path('product/<str:slug>/', produit_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    #path('produits/<str:slug>/update/', produit_update, name='product-update'),
    #path('produits/add/', produit_create , name='produit-create'),
    path('product/<str:slug>/delete/', produit_delete, name='product-delete'),
    path('contact-us/', contact, name='contact'),
    path('a-propos/', aPropos, name='a-propos'),
    path('cart/', cart, name='cart'),
    path('cart/delete', cart_delete, name='cart-delete'),

]
