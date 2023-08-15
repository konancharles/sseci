from django.db import models
from django.utils import timezone
 
# Create your models here.
class Universite(models.Model):
    name = models.CharField('Nom',unique = True, max_length=200)
    code = models.CharField('Code',unique = True, max_length=20)
    email = models.EmailField('Email',unique = True)
    contact = models.CharField('Contact',unique = True, max_length=20)
    
    class Meta:
        verbose_name_plural = 'Universités'

    def __str__(self):
        return self.name

class Sexe(models.Model):
    libelle = models.CharField('Libelle', max_length=20)


    class Meta:
        verbose_name_plural = 'Sexe'

    def __str__(self):
        return self.libelle


class Ufr(models.Model):
    name = models.CharField('Nom',unique = True, max_length=150)
    code = models.CharField('Code',unique = True, max_length=20)
    email = models.EmailField('Email',unique = True)
    contact = models.CharField('Contact',unique = True, max_length=20)
    universite = models.ForeignKey(Universite, verbose_name = 'Université',on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ufr'

    def __str__(self):
        return self.name


class Filiere(models.Model):

    libelle = models.CharField('libelle',unique = True, max_length=150)
    code = models.CharField('Code',unique = True, max_length=20)
    email = models.EmailField('Email',unique = True)
    contact = models.CharField('Contact',unique = True, max_length=20)
    ufr = models.ForeignKey(Ufr, verbose_name = 'Ufr',on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Filiere'

    def __str__(self):
        return self.libelle

# Register your models here (id_specialite,libelle,#id_ufr).

class Specialite(models.Model):
    libelle = models.CharField('libelle',unique = True, max_length=150)
    filiere = models.ForeignKey(Filiere, null = True, blank = True, verbose_name = 'Filiere',on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Specialité'

    def __str__(self):
        return self.libelle

# Register your models here Niveau (id_niveau,libelle)

class Niveau(models.Model):
    libelle = models.CharField('libelle',unique = True, max_length=150)
    class Meta:
        verbose_name_plural = 'Niveau'
    
    def __str__(self):
        return self.libelle


#Create your models here Niveau_specialite (id_niveau_specialite,#id_niveau,#id_specialite)
class NiveauSpecialite(models.Model):

    niveau = models.ForeignKey(Niveau, verbose_name = 'Niveau',on_delete = models.CASCADE)
    Specialite = models.ForeignKey(Specialite, verbose_name = 'Specialité',on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Niveau et Specialité'

    def __str__(self):
        return self.niveau

# Create your models here Ville (id_ville,libelle).
class Ville(models.Model):
    libelle = models.CharField('Libelle', unique=True, max_length = 60)

    class Meta:
     verbose_name_plural = 'Ville'
    def __str__(self):
        return self.libelle

#create your models here commune ( id_commune, #id_ville, libelle)
class Commune(models.Model):
    libelle = models.CharField('libelle', unique=True, max_length = 60)
    Ville = models.ForeignKey(Ville, verbose_name = 'Ville',on_delete = models.CASCADE)

    class Meta :
        verbose_name_plural= 'Commune'
    def __str__(self):
        return self.libelle

#Etudiant (id_etudiant,nom,prenom,matricule,lieu_de_naissance,date_de_naissance,email,contact,
#id_sexe,#id_ufr,#id_filiere,#id_specialite,#id_niveau,#id_ville,#id_commune,#id_univ)

class Etudiant(models.Model):

    name = models.CharField('Name', max_length=200)
    prenom = models.CharField('Prenom', max_length=20)
    email = models.EmailField('Email',unique = True, max_length=100)
    contact = models.CharField('Contact',unique = True, max_length=50)

    numero_cni = models.CharField('N°CNI',unique = True, null=True, blank=True, max_length=200)
    carte_etudiant = models.FileField('Carte d\'etudiant', upload_to = 'CarteEtudiant', null=True, blank=True, max_length=150)
    carte_cni = models.FileField('Carte NCI', upload_to = 'cni', null=True, blank=True, max_length=50)

    matricule = models.CharField('Matricule',unique = True, max_length=50 )
    lieu_de_naissance = models.CharField('Lieu de Naissance', max_length=20)
    date_de_naissance = models.DateField('Date de Naissance', max_length=20)
    sexe = models.ForeignKey(Sexe, verbose_name = 'Sexe',on_delete = models.CASCADE)
    ufr = models.ForeignKey(Ufr, verbose_name = 'Ufr',on_delete = models.CASCADE)
    filiere = models.ForeignKey(Filiere, verbose_name = 'Filière',on_delete = models.CASCADE)
    specialite = models.ForeignKey(Specialite, verbose_name = 'Specialité',on_delete = models.CASCADE)
    niveau = models.ForeignKey(Niveau, verbose_name = 'Niveau',on_delete = models.CASCADE)
    ville = models.ForeignKey(Ville, verbose_name = 'Ville',on_delete = models.CASCADE)
    commune = models.ForeignKey(Commune, verbose_name = 'Commune',on_delete = models.CASCADE)
    universite = models.ForeignKey(Universite, verbose_name = 'Université',on_delete = models.CASCADE)

    date = models.DateField('Date D\'identification', max_length=150, default = timezone.now )

    class Meta:
        verbose_name_plural = 'Etudiant'

    def __str__(self):
        return self.name





