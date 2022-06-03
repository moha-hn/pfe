from gestion.views import *
# from gestion.forms import activate_user
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    # accueil
    path('accueiletd/',accueiletd ,name='accueiletd'),
    path('accueilens/',accueilens ,name='accueilens'),
    path('accueiladmin/',accueiladmin ,name='accueiladmin'),
    # authentification
    path('',register ,name='register'),
    path('register_etd/',etudiant_register.as_view() ,name='register_etd'),
    path('register_ens/',enseignant_register.as_view() ,name='register_ens'),
    path('register_admin/',admin_register.as_view() ,name='register_admin'),
    path('loginetd/',login_viewetd ,name='loginetd'),
    path('loginens/',login_viewens ,name='loginens'),
    path('loginadmin/',login_viewadmin ,name='loginadmin'),
    path('logout/',logout_view ,name='logout'),
    # activer email
    path('activate_user/<uidb64>/<token>',activate_user,name='activate'),
    path('validation/<str:pk>/', validation, name="validation"),
    # gestion des comptes
    path('gestionetd/',gestionetd,name='gestionetd'),
    path('deleteetd/<str:pk>/', deleteetd, name="deleteetd"),
    path('gestionens/',gestionens,name='gestionens'),
    path('deleteens/<str:pk>/', deleteens, name="deleteens"),
    # cours
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('newcours/',newcours,name="newcours"),
    path('mescours/',mescours,name="mescours"),
    path('classroom/',classroom,name="classroom"),  
    path('categorie/',categorie,name="categorie"),
    path('categorie/<categorie_slug>',categoriecours,name="categoriecours"),
    path('<cours_id>/enroll',enroll,name="enroll"),
    path('<cours_id>/edit',editcours,name="editcours"),
    path('<cours_id>/delete',deletecours,name="deletecours"),
    path('direct/', include('direct.urls')),
    # update profile
    path('update/<str:pk>/', update , name="update"),
    path('updateetd/<str:pk>/', updateetd , name="updateetd"),
    path('updateens/<str:pk>/', updateens , name="updateens"),
    path('updateadmin/<str:pk>/', updateadmin , name="updateadmin"),
    path('home/',home,name="home"),
    # create section fac
    path('createsection/',createsection,name="createsection"),
    path('createfaculte/',createfaculte,name="createfaculte"),
    path('section/',sectiontable,name="section"),
    path('faculte/',facultetable,name="faculte"),
    path('deletesection/<str:pk>/', deletesection, name="deletesection"),
    path('deletefaculte/<str:pk>/', deletefaculte, name="deletefaculte"),
    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)