from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib import messages
from gestion.forms import *

from django.views.generic import CreateView
from django.contrib.auth import login, logout,authenticate

from .models import *
from django.contrib.auth.models import User
from django.db import transaction
from django.urls import reverse
from .forms import activate_user

from .filters import *
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
# view register
def register (request):
    return render (request,'index/index.html')
class etudiant_register(CreateView):
    model=user
    form_class=etudiantsignup
    template_name='log/registeretd.html'
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form
    def get_success_url(self):
        return reverse('loginetd')
    def validation(self,form):
        send_action_email(user,request)
        user=form.save()
        login(self.request,user)
        return redirect('loginetd')
class enseignant_register(CreateView):
    model=user
    form_class=enseignantsignup
    template_name='log/registerens.html'
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form
    def get_success_url(self):
        return reverse('loginens')
    def validation(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('loginens')

class admin_register(CreateView):
    model=user
    form_class=adminsignup
    template_name='log/registeradmin.html'
    def get_success_url(self):
        return reverse('loginadmin')
    def validation(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('loginadmin')


# login
def login_viewetd(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user.is_etudiant==True and  user is not None :
                # if not user.is_email_verified:
                #     messages.error(request,"email non validé, verifier votre boite mail.")
                # else:
                    login(request,user)
                    return redirect('accueiletd')
            else:
                messages.error(request,"email ou mot de passe invalide")
    else:
        messages.error(request,"email ou mot de passe invalide")
    return render(request,'log/loginetd.html',context={'form':AuthenticationForm()})

def login_viewens(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user.is_enseignant==True and user is not None :
                if not user.is_email_verified:
                    messages.error(request,messages.errors,"email non validé, verifier votre boite mail.")
                else:
                    login(request,user)
                    return redirect('accueilens')
            else:
                messages.error(request,"email ou mot de passe invalide")
    else:
        messages.error(request,"email ou mot de passe invalide")
    return render(request,'log/loginens.html',context={'form':AuthenticationForm()})

def login_viewadmin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user.is_superuser==True and user is not None :
                if not user.is_email_verified:
                    messages.error(request,"email non validé, verifier votre boite mail.")
                else: 
                    login(request,user)
                    return redirect('accueiladmin')
            else:
                messages.error(request,"email ou mot de passe invalide")
    else:
        messages.error(request,"email ou mot de passe invalide")
    return render(request,'log/loginadmin.html',context={'form':AuthenticationForm()})


# logout
def logout_view(request):
    logout(request)
    return redirect('/')


# accueil
def accueiletd(request):
    return render(request,'accueil/accueiletd.html')

def accueilens(request):
    return render(request,'accueil/accueilens.html')

def accueiladmin(request):
    return render(request,'accueil/accueiladmin.html')

# adminn gestion
def gestionetd(request):
    etd=user.objects.filter(is_etudiant=True)
    etf=etudiant.objects.all()
    myfilter=userfilter(request.GET ,queryset=etd)
    etd=myfilter.qs
    return render(request,'gestion/gestionetd.html',{'etd':etd,'etf':etf,'myfilter':myfilter})

def gestionens(request):
    ens=user.objects.filter(is_enseignant=True)
    ent=enseignant.objects.all()
    myfilter=userfilter(request.GET ,queryset=ens)
    ens=myfilter.qs
    return render(request,'gestion/gestionens.html',{'ens':ens,'ent':ent,'myfilter':myfilter})

def deleteetd(request,pk):
    item=user.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("gestionetd") 
    return render(request,'gestion/deleteetd.html',{'item':item})

def deleteens(request,pk):
    item=user.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("gestionens") 
    return render(request,'gestion/deleteens.html',{'item':item})

def validation(request,pk):
    stag=user.objects.filter(id=pk)
    form=validation(instance=stag)
    if request.method=='POST':
        form=validation(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("gestion") 
    return render(request,'validation.html',{'form':form})


# courss
def classroom(request):
    user=request.user
    cour=cours.objects.filter(inscrit=user)
    context={
        'cour':cour
    }
    return render(request,'class/class.html',context)

def categorie(request):
    categorie=categorie.objects.all()
    context={
        'categorie':categorie
    }
    return render(request,'class/categorie.html',context)

def categoriecours(request,ctegorie_slug):
    categorie=get_object_or_404(categorie, slug=categorie_slug)
    cours=cours.object.filter(categorie=categorie)
    context={
        'categorie':categorie,
        'cours':cours,
    }
    return render(request,'class/categoriecours.html',context)


def newcours(request):
    user=request.user
    if request.method=='POST':
        form=newcoursform(request.post,request.FILES)
        if form.is_valid():
            photo=form.cleaned_data.get('photo')
            titre=form.cleaned_data.get('titre')
            description=form.cleaned_data.get('description')
            categorie=form.cleaned_data.get('categorie')
            resume=form.cleaned_data.get('resume')
            cours.objects.create(photo=photo,titre=titre,description=description,categorie=categorie,resume=resume)
            return redirect('mescours')
    else:
        form=newcoursform()

    context= {
        'form':form
    }
    return render(request,'class/newcours.html',context)

@login_required
def enroll(request,cours_id):
    user=request.user
    cours=get_object_or_404(cours, id=cours_id)
    cours.inscrit.add(user)
    return redirect('index')

@login_required
def deletecours(request,cours_id):
    user=request.user
    cours=get_object_or_404(cours, id=cours_id)
    if user != cours.user:
        return HttpResponseForbidden()
    else:
        cours.delete()
    return redirect('mescours')

@login_required
def editcours(request,cours_id):
    user=request.user
    cours=get_object_or_404(cours, id=cours_id)
    if user != cours.user:
        return HttpResponseForbidden()
    else:
        if request.method=='POST':
            form=newcoursform(request.POST, request.FILES, instance=cours)
            if form.is_valid():
                photo=form.cleaned_data.get('photo')
                titre=form.cleaned_data.get('titre')
                description=form.cleaned_data.get('description')
                categorie=form.cleaned_data.get('categorie')
                resume=form.cleaned_data.get('resume')
                cours.save()
                return redirect('mescours')
        else:
            form=newcoursform(instance=cours)

    context={
        'form':form,
        'cours':cours,
    }
    return render(request,'class/editcours.html',context)

def mescours(request):
    user=request.user
    cours=cours.objects.filter(user=user)

    context={
        'cours':cours
    }
    return render(request,'class/mescours.html',context)

# profileee
def update(request,pk):
    stag=user.objects.get(id=pk)
    form=profilform(instance=stag)
    if request.method=='POST':
        form=profilform(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("gestionetd") 
    return render(request,'profil/updateprofil.html',{'form':form})

def updateetd(request,pk):
    stag=user.objects.get(id=pk)
    form=profilform(instance=stag)
    if request.method=='POST':
        form=profilform(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("accueiletd") 
    return render(request,'profil/updateprofiletd.html',{'form':form})

def updateens(request,pk):
    stag=user.objects.get(id=pk)
    form=profilform(instance=stag)
    if request.method=='POST':
        form=profilform(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("accueilens") 
    return render(request,'profil/updateprofilens.html',{'form':form})

def updateadmin(request,pk):
    stag=user.objects.get(id=pk)
    form=profilform(instance=stag)
    if request.method=='POST':
        form=profilform(data=request.POST,instance=stag)
        if form.is_valid():
            form.save()
            return redirect("accueiladmin") 
    return render(request,'profil/updateprofileadmin.html',{'form':form})

def  home(request):
    use=request.user
    if use.is_etudiant==True :
        return redirect("accueiletd")
    if use.is_enseignant==True :
        return redirect("accueilens")
    else :
        return redirect("accueiladmin")


# admin creation section faculte
def sectiontable(request):
    sec=section.objects.all()
    myfilter=sectionfilter(request.GET ,queryset=sec)
    sec=myfilter.qs
    return render(request,'create/section.html',{'sec':sec,'myfilter':myfilter})

def facultetable(request):
    sec=faculte.objects.all()
    myfilter=facultefilter(request.GET ,queryset=sec)
    sec=myfilter.qs
    return render(request,'create/faculte.html',{'sec':sec,'myfilter':myfilter})

def createsection(request):
    if request.method=='POST':
        form=sectionform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("section") 
        return render(request,'create/createsection.html',{'form':form})

    else :
     form= sectionform
     return render(request,'create/createsection.html',{'form':form})

def createfaculte(request):
    if request.method=='POST':
        form=faculteform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("faculte") 
        return render(request,'create/createfaculte.html',{'form':form})

    else :
     form= faculteform
     return render(request,'create/createfaculte.html',{'form':form})

def deletesection(request,pk):
    item=section.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("section") 
    return render(request,'create/deletesection.html',{'item':item})

def deletefaculte(request,pk):
    item=faculte.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("faculte") 
    return render(request,'create/deletefaculte.html',{'item':item})