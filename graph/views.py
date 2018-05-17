from django.http import HttpResponse

from django.shortcuts import render
from .forms import ContactForm
from django.db import models
 



"""def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid(): 

        utilisateur = form.cleaned_data['utilisateur']

        Password = form.cleaned_data['Password']

        email = form.cleaned_data['email']

        renvoi = form.cleaned_data['renvoi']

        envoi = True

    return render(request, 'projet/contact.html', locals())"""
def contact(request):
    sauvegarde = False
    form =ContactForm(request.POST or None)
    if form.is_valid():
        contact = Contact()
        contact.utilisateur = form.cleaned_data["utilisateur"]
        contact.Password = form.cleaned_data["Password"]
        contact.email = form.cleaned_data["email"]
        contact.save()
        sauvegarde = True

    return render(request, 'projet/contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })