from django.db import models
from django.contrib.auth.models import AbstractUser

    
class User(AbstractUser):
    
    FOURNISSEUR = 'FOURNISSEUR'
    CLIENT = 'CLIENT'

    ROLE_CHOICES = (
        (FOURNISSEUR, 'Fournisseur'),
        (CLIENT, 'Client'),
    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

