from django.shortcuts import render

# Create your views here.

def accueil(request) :
	''' vue qui renvoit la page d'accueil du site '''
	return render(request, 'signin_up/accueil.html', locals())