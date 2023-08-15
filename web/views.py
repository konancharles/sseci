from django.shortcuts import render , redirect
from urllib.request import Request 
from django.http import HttpRequest , HttpResponse , HttpResponseRedirect
from datetime import datetime 
from django.template import RequestContext
from django.template.context import Context
from django.http import JsonResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.template import loader
import random # cette commande demande a ce que les fichier importé ( ) soit nommé de manière aléatoire
import string # que le ,ommenclature soit un texte

def generate_random_file_name(length=20):
    """
    Générer des noms aléatoire pour les fichiers avant stockage   
    """
    letters = string.ascii_letters
    random_name = ''.join(random.choice(letters) for _ in range(length))
    return random_name

# Create your views here.
def accceuil(request):
    message = ""  #AJOUTER
    #print(Etudiant.objects.all())
    form = EtudiantForm()
    if request.methode == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            carte_etudiant_name = generate_random_file_name() + '.pdf'
            carte_cni_name = generate_random_file_name() + '.pdf'
            
            form.instance.carte_etudiant.name = carte_etudiant_name
            form.instance.carte_cni.name = carte_cni_name
            etudiant = form.save() #AJOUTER
            form = EtudiantForm()
            message = "success" #AJOUTER
        else:
            message = "error" #AJOUTER
            #print(form.errors)
    return render(request, 'app/index.html',{'form':form,'message': message })
            
            
    
    # récuperation de toutes les donnée de la table université. si on veu siblé un element universites = Universite.objects.get() 
   
    #return render(
   #     request, 
    #'app/index.html',
    #{
   #     'title' : 'système de suivi des étudiant de Côte d\'ivoire',
       
         
    #}
    #)
    
# s'il il y a une page contact on ferai les meme manip de acceuil pour celui-ci. ensuite on va dans urls.py definir le chemin d'acces idem de acceuil