from django.urls import path 
from django.views.generic.base import RedirectView
from . import views


#nom de l'appli...

app_name = 'web'
urlpatterns = [
    path ( '' , views.accceuil, name='acceuil' ),
    #path('service',views.services, name='services'),
    #path('Apropos',views.Apropos, name='Apropos'), CEUX-CI REPRESENTE LES PAGES D'ACCEUIL
]
