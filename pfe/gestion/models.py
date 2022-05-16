from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class administration (models.Model):
    nom=models.CharField(max_length=20)
    def __str__(self):
        return self.nom

class enseignant (models.Model):
    nom_utilisateur=models.CharField(max_length=50, primary_key=True)
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    SPECIALITE  = [
    ('INFO', 'Informatique'),
    ('PHY', 'physique'),
    ('CH', 'chimie '),
    ('BIO', 'Biologie'),
    ('GEO', 'Geologie'),
    ]
    specialite=models.CharField(choices=SPECIALITE,max_length=50)
    def __str__(self):
        return self.nom +' '+self.prenom

class section (models.Model):
    nom=models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return self.nom

class etudiant (models.Model):
    nom_utilisateur=models.CharField(max_length=50, primary_key=True)
    nom=models.CharField( max_length=50)
    prenom=models.CharField( max_length=50) 
    section=models.ForeignKey("section", on_delete=models.CASCADE)
    groupe=models.IntegerField( validators=[MinValueValidator(1),MaxValueValidator(6)])
    SPECIALITE  = [
    ('INFO', 'Informatique'),
    ('PHY', 'physique'),
    ('CH', 'chimie '),
    ('BIO', 'Biologie'),
    ('GEO', 'Geologie'),
    ]
    specialite=models.CharField(choices=SPECIALITE,max_length=50)
    def __str__(self):
        return self.nom + ' ' +self.prenom
    
class publication (models.Model):
    contenu=models.CharField(max_length=2500)
    date=models.DateField(default=timezone.now() ,editable=False)
    publieur=models.ForeignKey("enseignant", on_delete=models.CASCADE)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True)
    def __str__(self):
        return self.publieur

class module (models.Model):
    nom=models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class message (models.Model):
    contenu=models.CharField(max_length=250)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE)
    etudiant=models.ForeignKey("etudiant", on_delete=models.CASCADE,blank=True)
    administration=models.ForeignKey("administration", on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.emetteur

class commentaire (models.Model):
    contenu=models.CharField(max_length=250)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE,blank=True)
    etudiant=models.ForeignKey("etudiant", on_delete=models.CASCADE,blank=True)
    date=models.DateField(default=timezone.now() ,editable=False)
    heure=models.TimeField(default=timezone.now())
    def __str__(self):
        return str(self.publieur)

class note (models.Model):
    note=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(20)])
    etudiant_note=models.ForeignKey("etudiant", on_delete=models.CASCADE)
    enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE )
    def __str__(self):
         return self.note
