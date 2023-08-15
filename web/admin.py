from django.contrib import admin
from .models import *
# Register your models here.

class UniversiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'email', 'contact']
    search_fields = ['name']


class SexeAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

class UfrAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'email', 'contact', 'universite']
    search_fields = ['name']


 # Register your models here (id_filiere,code,name,email,contact,#id_ufr).

class FiliereAdmin(admin.ModelAdmin):
    list_display = ['code', 'libelle', 'email', 'contact', 'ufr']
    search_fields = ['libelle']

# Register your models here (id_specialite,libelle,#id_ufr).

class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'filiere']
    search_fields = ['libelle']


admin.site.register(Specialite, SpecialiteAdmin)

# Register your models here Niveau (id_niveau,libelle).
class NiveauAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Niveau, NiveauAdmin)

#Create your models here Niveau_specialite (id_niveau_specialite,#id_niveau,#id_specialite)
class NiveauSpecialiteAdmin(admin.ModelAdmin):
    list_display = ['niveau','Specialite']
    search_fields = ['niveau']

admin.site.register(NiveauSpecialite, NiveauSpecialiteAdmin)

#create your models here Ville (id_ville, libelle)
class VilleAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Ville, VilleAdmin)

#create your models here commune ( id_commune, #id_ville, libelle)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Commune, CommuneAdmin)

#Etudiant (id_etudiant,nom,prenom,matricule,lieu_de_naissance,date_de_naissance,email,contact,
#id_sexe,#id_ufr,#id_filiere,#id_specialite,#id_niveau,#id_ville,#id_commune,#id_univ)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['name', 'prenom', 'email', 'contact', 'matricule', 'lieu_de_naissance', 'date_de_naissance', 'sexe','ufr',
    'filiere', 'specialite', 'niveau', 'ville', 'commune', 'universite', 'numero_cni', 'carte_etudiant', 'carte_cni', 'date']
    search_fields = ['name']

admin.site.register(Etudiant, EtudiantAdmin)




#*******************************************************************************************************************************
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Ufr, UfrAdmin)
admin.site.register(Sexe, SexeAdmin)
admin.site.register(Universite, UniversiteAdmin)




