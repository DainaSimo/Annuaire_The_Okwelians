import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import (
    General, Lauréats, Membre_De_La_Family, Membre_Adhérents, 
    Partenaires, Elders, Autres, Mentors, Utilisateur, Bénévoles, personne_ressource
)

def apply_filters(queryset, filters):
    """Helper function to apply filters to any queryset"""
    for field, value in filters.items():
        if value:
            queryset = queryset.filter(**{f"{field}__icontains": value})
    return queryset

def export_to_excel(data_query, filename="export.xlsx"):
    """Helper function to export queryset to Excel"""
    if not data_query.exists():
        return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
    
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    df = pd.DataFrame(list(data_query.values()))
    cols = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    df_selection = df.iloc[:, cols]
    
    with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
        df_selection.to_excel(writer, index=False, sheet_name='Données')
    return response

def List_Général(request):
    contacts = General.objects.all()
    professions = contacts.values_list('profession', flat=True).distinct().exclude(profession='').order_by('profession')
    
    search_query = request.GET.get('recherche', '')
    selected_profession = request.GET.get('profession', '')
    
    if search_query:
        contacts = contacts.filter(
            Q(nom__icontains=search_query) |
            Q(prénom__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(téléphone1__icontains=search_query) |
            Q(structure__icontains=search_query) |
            Q(secteur__icontains=search_query) |
            Q(secteur_activité__icontains=search_query) |
            Q(pays_de_résidence__icontains=search_query) |
            Q(ville_de_résidence__icontains=search_query) |
            Q(région_origine__icontains=search_query)
        )
    
    if selected_profession:
        contacts = contacts.filter(profession=selected_profession)

    # Ajout de la pagination
    paginator = Paginator(contacts, 12)  # 10 cards par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': search_query,
        'professions': professions,
        'selected_profession': selected_profession,
    }
    return render(request, 'Contacts/Accueil.html', context)
   

    

def Liste_lauréats(request):
    data_query = Lauréats.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    programme = request.GET.get('programme', None)
    année = request.GET.get('année', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if programme:
        data_query = data_query.filter(programme__icontains=programme)
    if année:
        data_query = data_query.filter(année__icontains=année)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Lauréats.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        Lauréat = Lauréats.objects.all().order_by('id_lauréat')
        paginator = Paginator(Lauréat, 2) 
        page_number = request.GET.get('Lauréats')
        page_obj = paginator.get_page(page_number) 
    
    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Lauréats, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.programme = request.POST["ville_de_résidence"]
        row.année = request.POST["région_origine"]
        row.save()

        return redirect("Liste_lauréats")  # Recharge la page après modification

   
   

    return render(request, 'Contacts/Lauréats.html', {'page_obj': page_obj, 'query': query})

def Liste_membre_de_la_family(request):
    data_query = Membre_De_La_Family.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Membre_De_La_Family.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        Family = Membre_De_La_Family.objects.all().order_by('id_family')
        paginator = Paginator(Family, 2) 
        page_number = request.GET.get('Membre_De_La_Family')
        page_obj = paginator.get_page(page_number) 

    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Membre_De_La_Family, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.save()

        return redirect("Liste_membre_de_la_family")  # Recharge la page après modification
   

    return render(request, 'Contacts/Membre_de_la_family.html', {'page_obj': page_obj, 'query': query})
   

def Liste_membre_adhérent(request):

    data_query = Membre_Adhérents.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Membre_Adhérents.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        Adhérent = Membre_Adhérents.objects.all().order_by('id_membre')
        paginator = Paginator(Adhérent, 2) 
        page_number = request.GET.get('Membre_Adhérents')
        page_obj = paginator.get_page(page_number) 
    
    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Membre_Adhérents, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.save()

        return redirect("Liste_membre_adhérent")  # Recharge la page après modification
   

    return render(request, 'Contacts/Membre_adhérent.html', {'page_obj': page_obj, 'query': query})

def Liste_partenaire(request):

    data_query = Partenaires.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Partenaires.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        partenaire = Partenaires.objects.all().order_by('id_partenaire')
        paginator = Paginator(partenaire, 2) 
        page_number = request.GET.get('Partenaires')
        page_obj = paginator.get_page(page_number) 

    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Partenaires, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.save()

        return redirect("Liste_partenaire")
   

    return render(request, 'Contacts/Partenaire.html', {'page_obj': page_obj, 'query': query})
    

def Liste_elders(request):

    data_query = Elders.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Elders.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        elder = Elders.objects.all().order_by('id_elder') 
        paginator = Paginator(elder, 2) 
        page_number = request.GET.get('Elders')
        page_obj = paginator.get_page(page_number) 
   

    return render(request, 'Contacts/Elders.html', {'page_obj': page_obj, 'query': query})


def Liste_autres(request):
    data_query = Autres.objects.all()
    memberships = data_query.values_list('membership', flat=True).distinct().exclude(membership='').order_by('membership')

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    membership = request.GET.get('membership', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)
    if membership:
        data_query = data_query.filter(membership__icontains=membership)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Autres.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        Membership = Autres.objects.all().order_by('id_autre')
        paginator = Paginator(Membership, 2) 
        page_number = request.GET.get('Autres')
        page_obj = paginator.get_page(page_number) 
    
    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Autres, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.membership = request.POST["membership"]
        row.save()

        return redirect("Autres")  # Recharge la page après modification

    return render(request, 'Contacts/Autres.html', {'page_obj': page_obj, 'query': query, 'memberships' : memberships})
    
def Bénévoles(request):
    return render(request, 'Contacts/Bénévoles.html')

def Liste_personne_ressource(request):
    return render(request, 'Contacts/personne_ressource.html')

def Mentor(request):
    data_query = Mentors.objects.all()

    diplôme = request.GET.get('diplôme', None)
    région_origine = request.GET.get('région_origine', None)
    programme = request.GET.get('programme', None)
    année_intervention = request.GET.get('année_intervention', None)
    sexe = request.GET.get('sexe', None)
    age = request.GET.get('age', None)
    profession = request.GET.get('profession', None)
    secteur = request.GET.get('secteur', None)
    secteur_activité = request.GET.get('Secteur_activité', None)
    pays_de_résidence = request.GET.get('pays_de_résidence', None)
    région_de_résidence = request.GET.get('région_de_résidence', None)
    département_de_résidence = request.GET.get('département_de_résidence', None)
    
    
    if diplôme:
        data_query = data_query.filter(diplôme__icontains=diplôme)
    if région_origine:
        data_query = data_query.filter(région_origine__icontains=région_origine)
    if programme:
        data_query = data_query.filter(programme__icontains=programme)
    if année_intervention:
        data_query = data_query.filter(année_intervention__icontains=année_intervention)
    if sexe:
        data_query = data_query.filter(sexe__icontains=sexe)
    if age:
        data_query = data_query.filter(age__icontains=age)
    if profession:
        data_query = data_query.filter(profession__icontains=profession)
    if secteur:
        data_query = data_query.filter(secteur__icontains=secteur)
    if secteur_activité:
        data_query = data_query.filter(secteur_activité__icontains=secteur_activité)
    if pays_de_résidence:
        data_query = data_query.filter(pays_de_résidence__icontains=pays_de_résidence)
    if région_de_résidence:
        data_query = data_query.filter(région_de_résidence__icontains=région_de_résidence)
    if département_de_résidence:
        data_query = data_query.filter(département_de_résidence__icontains=département_de_résidence)

    try:
        limite = int(request.GET.get('entier', 10))
    except ValueError:
        limite = 10 

    data_query = data_query[:int(limite)]
    if request.GET.get('export') == '1':
        data = list(data_query.values())
        df = pd.DataFrame(data)
        df_selection = df.iloc[:, [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
        
        if df.empty:
            return HttpResponse("Aucune donnée à exporter.", content_type="text/plain")
        
        else:
            response = HttpResponse(content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachement; filename = "Lauréat.xlsx"'

            with pd.ExcelWriter(response, engine='xlsxwriter') as writer:
                df_selection.to_excel(writer, index=False, sheet_name='Données')
            return response
    
    query = request.GET.get('recherche', '')  # Récupérer la valeur du champ de recherche
    if query:
        page_obj = Mentors.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        mentor = Mentors.objects.all().order_by('id_mentor')
        paginator = Paginator(mentor, 2) 
        page_number = request.GET.get('Mentors')
        page_obj = paginator.get_page(page_number) 
    
    if request.method == "POST":
        emails = request.POST.get("email")
        row = get_object_or_404(Mentorss, email=emails)

        # Mettre à jour les informations du contact
        row.prénom = request.POST["prénom"]
        row.nom = request.POST["nom"]
        row.téléphone1 = request.POST["téléphone1"]
        row.email = request.POST["email"]
        row.diplôme = request.POST["diplôme"]
        row.sexe = request.POST["sexe"]
        row.age = request.POST["age"]
        row.profession = request.POST["profession"]
        row.structure = request.POST["structure"]
        row.secteur = request.POST["secteur"]
        row.secteur_activité = request.POST["secteur_activité"]
        row.pays_de_résidence = request.POST["pays_de_résidence"]
        row.région_de_résidence = request.POST["région_de_résidence"]
        row.département_de_résidence = request.POST["département_de_résidence"]
        row.ville_de_résidence = request.POST["ville_de_résidence"]
        row.région_origine = request.POST["région_origine"]
        row.programme = request.POST["programme"]
        row.année = request.POST["année_intervention"]
        row.save()

        return redirect("Mentor")  # Recharge la page après modification

   
   

    return render(request, 'Contacts/Mentor.html', {'page_obj': page_obj, 'query': query})



def connexion_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            utilisateur = Utilisateur.objects.get(username=username)
            if utilisateur.mot_de_passe == password:
                # Authentification manuelle réussie
                request.session['utilisateur_id'] = utilisateur.ID_user
                request.session['username'] = utilisateur.username
                return redirect('List_Général')  # à adapter
            else:
                messages.error(request, "Mot de passe incorrect.")
        except Utilisateur.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")

    return render(request, 'Contacts/connexion.html')


