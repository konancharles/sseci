from django import forms 

from .models import Etudiant # IMPORTER LE MODEL



class EtudiantForm(forms.ModelForm): # STOCKER LE MODEL DANS LE CHAMPS
    class Meta: 
        model = Etudiant
        fields = (
            'nom', 'prenom','email','contact','numero_cni','carte_cni', 'carte_etudiant''matricule','lieu_de_naissance','date_de_naissance', 'sexe', 'ufr', 'filiere', 'specialite', 'niveau', 'commune', 'universite', 'ville'
        )
        Widgets = {
            'nom' : forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Nom'}),
            'prenom' : forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Prenom'}),
            'email' : forms.EmailInput(attrs={'class': 'from-control', 'placeholder': 'Email'}),
            'contact' : forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Contact'}),
            'numero_cni' : forms.FileInput(attrs={'class': 'from-control', 'placeholder': 'Numero CNI'}),
            'carte_etudiant' : forms.FileInput(attrs={'class': 'from-control', 'placeholder': 'Catre d\'Etudiant'}),
            'carte_cni' : forms.FileInput(attrs={'class': 'from-control', 'placeholder': 'Catre CNI'}),
            'matricule' : forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Matricule'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'Matricule'}),
            'date_de_naissance' : forms.DateInput(attrs={'class': 'from-control', 'placeholder': 'Matricule'}),
            'sexe' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Matricule'}),
            'ufr' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Ufr'}),
            'filiere' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Filiere'}),
            'sepecialite' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Specialite'}),
            'niveau' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Niveau'}),
            'commune' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Commune'}),
            'universite' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Universite'}),
            'ville' : forms.Select(attrs={'class': 'from-control', 'placeholder': 'Ville'}),
            
            
            
            
        }