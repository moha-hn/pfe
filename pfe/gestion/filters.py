import django_filters
from .models import *

class userfilter(django_filters.FilterSet):
    class Meta:
        model=user
        fields=['username','email','nom','prenom']

class sectionfilter(django_filters.FilterSet):
    class Meta:
        model=section
        fields=('__all__')

class facultefilter(django_filters.FilterSet):
    class Meta:
        model=faculte
        fields=('__all__')
