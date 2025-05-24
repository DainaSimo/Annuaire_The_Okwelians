
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.connexion_view, name='connexion_view'),
    path('connexion/', views.connexion_view, name='connexion_view'),
    path('List_Général/', views.List_Général, name='List_Général'),
    path('Lauréats/', views.Liste_lauréats, name='Liste_lauréats'),
    path('Membre_de_la_family/', views.Liste_membre_de_la_family, name='Liste_membre_de_la_family'),
    path('Membre_adhérent/', views.Liste_membre_adhérent, name='Liste_membre_adhérent'),
    path('Partenaire/', views.Liste_partenaire, name='Liste_partenaire'),
    path('Elders/', views.Liste_elders, name='Liste_elders'),
    path('Autres/', views.Liste_autres, name='Liste_autres'),
    path('Bénévoles/', views.Bénévoles, name='Bénévoles'),
    path('personne_ressource/', views.Liste_personne_ressource, name='Liste_personne_ressource'),
    path('Mentor/', views.Mentor, name='Mentor')
]
