from django.forms import ModelForm
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from .utils import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth import get_user_model

# Email verification+activation du compte
def send_action_email(user,request):
    current_site=get_current_site(request)
    email_subject='Activer votre compte'
    email_body=render_to_string('auth/activate.html',{
        'user':user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user)
        })
    
    email=EmailMessage(subject=email_subject,body=email_body,
                from_email=settings.EMAIL_FROM_USER,
                to=[user.email]
                )

    email.send()

def activate_user(request,uidb64,token):
    try: 
        uid=force_str(urlsafe_base64_decode(uidb64))
        User=get_user_model()
        user=User.objects.get(pk=uid)
    
    except Exception as e:
        user=None

    if user and generate_token.check_token(user,token):
        user.is_email_verified=True
        user.save()
        messages.add_message(request,messages.SUCCESS,'Email validé')
        if user.is_etudiant==True:
            return redirect(reverse('loginetd'))
        elif user.is_enseignant== True:
            return redirect(reverse('loginens'))
        else:
            return redirect(reverse('loginadmin'))
    else:
        return render(request,'auth/activate-failed.html',{"user":user})


# Authentification
class etudiantsignup(UserCreationForm):
    nom=forms.CharField(required=True)
    prenom=forms.CharField( required=True)
    email=forms.EmailField( required=True)
    section_set=section.objects.all()
    section=forms.ModelChoiceField(queryset=section_set)
    groupe=forms.IntegerField(required=True,validators=[MinValueValidator(1),MaxValueValidator(6)])
    class Meta(UserCreationForm.Meta):
        model=user
    
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_etudiant=True
        user.email=self.cleaned_data.get('email')
        user.nom=self.cleaned_data.get('nom')
        user.prenom=self.cleaned_data.get('prenom')
        user.save()
        etd=etudiant.objects.create(user=user,section=self.cleaned_data.get('section'),groupe=self.cleaned_data.get('groupe'))
        etd.save()
        # send_action_email(user,self.request)
        return etd

class enseignantsignup(UserCreationForm):
    nom=forms.CharField(required=True)
    prenom=forms.CharField( required=True)
    email=forms.EmailField(required=True)
    fac_set=faculte.objects.all()
    faculte=forms.ModelChoiceField(queryset=fac_set)
    grd_set=grade.objects.all()
    grade=forms.ModelChoiceField(queryset=grd_set)
    class Meta(UserCreationForm.Meta):
        model=user

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_enseignant=True
        user.email=self.cleaned_data.get('email')
        user.nom=self.cleaned_data.get('nom')
        user.prenom=self.cleaned_data.get('prenom')
        user.save()
        ens=enseignant.objects.create(user=user,faculte=self.cleaned_data.get('faculte'),grade=self.cleaned_data.get('grade'))
        ens.save()
        # send_action_email(user,self.request)
        return ens
        
class adminsignup(UserCreationForm):
    nom=forms.CharField(required=True)
    prenom=forms.CharField( required=True)
    email=forms.EmailField(required=True)
    fac_set=faculte.objects.all()
    faculte=forms.ModelChoiceField(queryset=fac_set)
    class Meta(UserCreationForm.Meta):
        model=user

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_superuser=True
        user.email=self.cleaned_data.get('email')
        user.nom=self.cleaned_data.get('nom')
        user.prenom=self.cleaned_data.get('prenom')
        user.save()
        ens=administration.objects.create(user=user,faculte=self.cleaned_data.get('faculte'))
        ens.save()
        send_action_email(user,self.request)
        return ens


# classs
class newcoursform(forms.ModelForm):
    photo=forms.ImageField(required=True)
    titre=forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}), required=True)
    decription=forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}), required=True)
    categorie=forms.ModelChoiceField(queryset=categorie.objects.all())
    resume=forms.CharField(widget=CKEditorWidget())

    class Meta:
        model=cours
        fields=('__all__')



class profilform(ModelForm):
   class Meta:
       model=user 
       fields=['username','email','nom','prenom']

# admin section faculte
class sectionform(ModelForm):
    class Meta:
        model=section
        fields=('__all__')

class faculteform(ModelForm):
    class Meta:
        model=faculte
        fields=('__all__')
