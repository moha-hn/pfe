from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from ckeditor.fields import RichTextField

# premiere partie (signup register)

    
class etablissement(models.Model):
    nom=models.CharField(max_length=50)
    def __str__(self):
        return self.nom
    
class faculte(models.Model):
    nom=models.CharField(max_length=50)
    etablissement=models.ForeignKey("etablissement", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
class section (models.Model):
    nom=models.CharField(max_length=20)
    faculte=models.ForeignKey("faculte", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class user(AbstractUser):
    is_etudiant=models.BooleanField(default=False)
    is_enseignant=models.BooleanField(default=False)
    email=models.EmailField(max_length=254)
    is_email_verified=models.BooleanField(default=False)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)


    

class etudiant(models.Model):
    user=models.OneToOneField(user, on_delete=models.CASCADE)
    section=models.ForeignKey("section", on_delete=models.CASCADE,blank=True)
    groupe=models.IntegerField( validators=[MinValueValidator(1),MaxValueValidator(6)],blank=True)
    def __str__(self):
        return self.nom+' '+self.prenom

class grade(models.Model):
    GRADE_ENS  = [
    ('Maitre Assisstant a', 'Maitre Assisstant a'),
    ('Maitre Assisstant b', 'Maitre Assisstant b'),
    ('Maitre Conference a', 'Maitre Conference a'),
    ('Maitre Conference b', 'Maitre Conference b'),
    ('Professeur', 'Professeur'),]
    grade=models.CharField(choices=GRADE_ENS, max_length=50)
    def __str__(self):
        return self.grade

class enseignant(models.Model):
    user=models.OneToOneField(user, on_delete=models.CASCADE)
    grade=models.ForeignKey("grade", on_delete=models.CASCADE)
    faculte=models.ForeignKey("faculte", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom+' '+self.prenom

class administration(models.Model):
    user=models.OneToOneField(user, on_delete=models.CASCADE)
    faculte=models.ForeignKey("faculte", on_delete=models.CASCADE)
    def __str__(self):
        return self.nom+' '+self.prenom

# deuxieme partie(module)
class module(models.Model):
    title=models.CharField(max_length=50)
    user=models.ForeignKey(user, on_delete=models.CASCADE,related_name='module_owner')
    hours=models.PositiveIntegerField()

    def _str_(self):
        return self.title

# class
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class categorie(models.Model):
    titre=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    def get_absolute_url(self):
        return reverse('categries',arg=[self.slug])
    def __str__(self):
        return self.titre
    
    
class cours(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo=models.ImageField(upload_to=user_directory_path)
    titre=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    categorie=models.ForeignKey(categorie,on_delete=models.CASCADE)
    resume=RichTextField()
    user=models.ForeignKey(user, on_delete=models.CASCADE,related_name='cours_owner')
    inscrit=models.ManyToManyField('user')
    section=models.ForeignKey("section", on_delete=models.CASCADE)
    faculté=models.ForeignKey("faculte", on_delete=models.CASCADE)
    def __str__(self):
        return self.titre+'('+self.section+')'
    







# class publication (models.Model):
#     contenu=models.CharField(max_length=2500)
#     date=models.DateField(auto_now_add=True,editable=False)
#     section=models.ForeignKey("section", on_delete=models.CASCADE)
#     publieur=models.ForeignKey(User, verbose_name='Owner',on_delete=models.CASCADE)
#     image=models.ImageField(blank=True, upload_to='none')
#     file=models.FileField(blank=True)

# class module (models.Model):
#     nom=models.CharField(max_length=50)
#     section=models.ForeignKey("section", on_delete=models.CASCADE)
#     def __str__(self):
#         return self.nom

# class message (models.Model):
#     contenu=models.CharField(max_length=250)
#     date=models.DateField(auto_now_add=False)
#     heure=models.TimeField(auto_now_add=False)
#     expediteur=models.ForeignKey(User, verbose_name='owner', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.emetteur

# class commentaire (models.Model):
#     contenu=models.CharField(max_length=250)
#     enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE,blank=True)
#     etudiant=models.ForeignKey("etudiant", on_delete=models.CASCADE,blank=True)
#     date=models.DateField(default=timezone.now() ,editable=False)
#     heure=models.TimeField(default=timezone.now(),editable=False)
#     def __str__(self):
#         return str(self.enseignant)

# class note (models.Model):
#     note=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(20)])
#     enseignant=models.ForeignKey("enseignant", on_delete=models.CASCADE )
#     def __str__(self):
#          return str(self.note)
