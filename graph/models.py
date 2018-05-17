from django.db import models


class Contact(models.Model):

    utilisateur = models.CharField(max_length=255)

    email = models.EmailField(max_length=254)

    Password = models.CharField(max_length=255)

    

    def __str__(self):

           return self.utilisateur