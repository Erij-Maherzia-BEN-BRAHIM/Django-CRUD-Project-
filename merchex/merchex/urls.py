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
from django.urls import path
from listings import views
from django.contrib.auth.views import LoginView , LogoutView , PasswordChangeDoneView, PasswordChangeView
import authentification.views


urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
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
    path('fournisseurs/', views.fournisseur_list , name='fournisseur-list'),
    path('fournisseurs/<int:id>/', views.fournisseur_detail, name='fournisseur-detail'),
    path('fournisseurs/<int:id>/update/', views.fournisseur_update, name='fournisseur-update'),
    path('fournisseurs/<int:id>/delete/', views.fournisseur_delete, name='fournisseur-delete'),
    path('fournisseurs/add/', views.fournisseur_create , name='fournisseur-create'),
    path('produits/', views.produit_list, name='produit-list'),
    path('produits/<int:id>/', views.produit_detail, name='produit-detail'),
    path('produits/<int:id>/update/', views.produit_update, name='produit-update'),
    path('produits/add/', views.produit_create , name='produit-create'),
    path('produits/<int:id>/delete/', views.produit_delete, name='produit-delete'),
    path('contact-us/', views.contact, name='contact'),
    path('a-propos/', views.aPropos, name='a-propos'),
  
]
