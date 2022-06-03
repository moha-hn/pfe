from django.contrib import admin
from gestion.models import *

admin.site.register(user)
admin.site.register(section)
admin.site.register(etudiant)
admin.site.register(enseignant)
admin.site.register(administration)
admin.site.register(cours)
admin.site.register(etablissement)
admin.site.register(faculte)
admin.site.register(grade)
class categorieadmin (admin.ModelAdmin):
    prepopulated_fields={"slug":("titre",)}

admin.site.register(categorie,categorieadmin)
    


# admin.site.register(publication)
# admin.site.register(module)

