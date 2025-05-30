import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector

# 1) Configuration de google sheet

champ_application = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
References = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", champ_application)
client = gspread.authorize(References)

# Ouverture du classeur
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/10-BCkQZltFQWibW4gFz9Wfj8dED4-hEVjwcBNRf7FKM/edit?usp=sharing")
worksheet = spreadsheet.worksheet('Réponses au formulaire 3')

# Lire les données
records = worksheet.get_all_records()
df = pd.DataFrame(records)


df


#Transformer les données

df['nom'] = df['nom'].str.upper()
df['prénom'] = df['prénom'].str.capitalize()
df["diplome"] = df['diplome'].replace({"Master / Master's degree" : "Master",
                                       "Licence / Bachelor's degree" : "Licence",
                                       'Baccalauréat / GCE "A" Level' : "Baccalauréat",
                                       'BEPC / GCE "O" Level' : "BEPC",
                                       "BTS / Advanced Technician's Certificate" : "BTS",
                                       "DUT / Two-year university degree in technology" : "DUT",
                                       "Doctorat / PhD" : "Doctorat",
                                       "Diplôme d'ingénieur / Engineering degree" : "Diplôme d'ingénieur",
                                       "GCE Alevel" : "Baccalauréat",
                                       "Master 2" : "Master",
                                       "Bac+3" : "Licence",
                                       "GCE A/L" : "Baccalauréat",
                                       "Master1 " : "Maîtrise",
                                       "GCE A level" : "Baccalauréat",
                                       "Doctor of Medicine degree " : "Doctorat (Santé)",
                                       "Master 2 Gestion des Ressources Humaines " : "Master",
                                       "B.e.p.c" : "BEPC",
                                       "Ingénieur de conception en maintenance industrielle et productique" : "Diplôme d'ingénieur",
                                       "Licence en Audit et contrôle " : "Licence",
                                       "ingénieur de conception pétrole et gaz " : "Diplôme d'ingénieur",
                                       "Bts cge" : "BTS",
                                       "Mastère Spécialisé en marché des énergies" : "Master",
                                       "Master en sociologie" : "Master",
                                       "Ingénieur Halieute" : "Diplôme d'ingénieur",
                                       "Baccalauréat A4" : "Baccalauréat",
                                       "Master's Degree" : "Master",
                                       "Master II" : "Master",
                                       "Master 1 en droit et administration publique" : "Maîtrise",
                                       "Master II en Marketing" : "Master",
                                       "Bac +3 en Informatique" : "Licence",
                                       "Bsc in Marketing" : "Licence",
                                       "MASTER 2 EN SCIENCE DE GESTION - COMPTABILITÉ CONTRÔLE AUDIT" : "Master",
                                       "Licence en lettes d'expression Française" : "Licence",
                                       "Diplôme d'ingénieur de conception" : "Diplôme d'ingénieur",
                                       "Ingénieur de Conception en Génie Mécanique" : "Diplôme d'ingénieur",
                                       "MSc in International Business and Management" : "Master",
                                       "Master II recherche" : "Master",
                                       "BACCALAUREAT" : "Baccalauréat",
                                       "Bts" : "BTS",
                                       "MASTER" : "Master",
                                       "Master 2 en eau hygiène et assainissement" : "Master",
                                       "Bachelors degree" : "Licence",
                                       "Ingénieur" : "Diplôme d'ingénieur",
                                       "Diplôme d'ingénieur de conception" : "Diplôme d'ingénieur",
                                       "Licence Professionnelle" : "Licence",
                                       "Licence en physique mécanique" : "Licence",
                                       "Ingénieur" : "Diplôme d'ingénieur",
                                       "INGÉNIEUR DE CONCEPTION EN GÉNIE INFORMATIQUE" : "Diplôme d'ingénieur",
                                       "Licence en géographie physique" : "Licence",
                                       "Bac+3" : "Licence",
                                       "Master en Droit Public" : "Master",
                                       "Master 2 en psychologie" : "Master",
                                       "Licence en géographie humaine" : "Licence",
                                       "Master 2 Stratégie et Communication des marques" : "Master",
                                       "EMBA" : "Master",
                                       "Master Professionnel en maintenance et gestion des systèmes énergétiques" : "Master",
                                       "Diplôme d'ingénieur des travaux des télécommunications option informatique et réseaux" : "Diplôme d'ingénieur",
                                       "Master de spécialisation" : "Master",
                                       "Diplôme d'ingénieur en Génie Industriel" : "Diplôme d'ingénieur",
                                       "doctorat" : "Doctorat",
                                       "Master II Computer Science" : "Master",
                                       "MASTER 2 EN MANAGEMENT - Master 2 en ingenierie" : "Diplôme d'ingénieur",
                                       "Post graduate dimplomat" : "Master"})

df["sexe"] = df['sexe'].replace({"Une femme / A woman" : "Une femme",
                                 "Un homme / A man" : "Un homme"})

df["region_de_residence"] = df['region_de_residence'].replace({"Ouest / West" : "Ouest",
                                                     "Littoral / Littoral" : "Littoral",
                                                     "Est / East" : "Est",
                                                     "Centre / Center" : "Centre",
                                                     "Sud / South" : "Sud",
                                                     "Sud-Ouest / South-West" : "Sud-Ouest",
                                                     "Extrême Nord / Farth-North" : "Extrême-Nord",
                                                     "Nord / North" : "Nord",
                                                     "Nord-ouest / North-West" : "Nord-Ouest",
                                                     "Adamaoua / Adamaowa" : "Adamaoua"
                                                    })

df["region_origine"] = df['region_origine'].replace({"Ouest / West" : "Ouest",
                                                     "Littoral / Littoral" : "Littoral",
                                                     "Est / East" : "Est",
                                                     "Centre / Center" : "Centre",
                                                     "Sud / South" : "Sud",
                                                     "Sud-Ouest / South-West" : "Sud-Ouest",
                                                     "Extrême Nord / Farth-North" : "Extrême-Nord",
                                                     "Nord / North" : "Nord",
                                                     "Nord-ouest / North-West" : "Nord-Ouest",
                                                     "Adamaoua / Adamaowa" : "Adamaoua"
                                                    })

df["secteur"] = df['secteur'].replace({"Privé / Private" : "Privé",
                                                     "Public / Public" : "Public"
                                                    
                                                    })

df["secteur_activite"] = df['secteur_activite'].replace({"Economie/ Economy" : "Economie",
                                                     "Santé/ Health" : "Santé",
                                                         "ICT / Software Engineering" : "Informatique",
                                                         "Communication/ Communication" : "Communication",
                                                         "Education supérieure" : "Education",
                                                         "Environmental Sciences" : "Environment",
                                                         "Tech" : "Informatique",
                                                         "Agriculture/ Agriculture" : "Agriculture",
                                                         "Enseignement" : "Éducation",
                                                         "Non-travailleur" : "Chomage",
                                                         "NA" : "Chomage",
                                                         "Éducatif" : "Éducation",
                                                         "Aucune" : "Chomage",
                                                         "Technologie de l'information " : "Informatique",
                                                         "Education" : "Éducation",
                                                         "TIC" : "Informatique",
                                                         "INFORMATIQUE -TIC" : "Informatique",
                                                         "Politique/ Politics" : "Politique",
                                                         "ENSEIGNEMENT" : "Éducation",
                                                         "IT" : "Informatique",
                                                         "Civil society" : "société civile",
                                                         "Informatique et technologies" : "Informatique",
                                                         "Débrouille" : "Chomage"
                                                    })


df["profession"] = df['profession'].replace({"Étudiante" : "Étudiant",
                                                     "Au chômage " : "Sans emploi",
                                             "En recherche d'emploi" : "Sans emploi",
                                             "Aucune" : "Sans emploi",
                                             "Étudiant en ingénierie informatique" : "Étudiant",
                                             "Sans profession" : "Sans emploi",
                                             "Étudiants en master intégration régionale et management des institutions communautaires a l'IRIC .par ailleurs président de ORESAH ( ORGANISATION POUR LA RÉSILIENCE SOCIO-ÉCONOMIQUE ET L'ASSISTANCE HUMANITAIRE),RESPONSABLE RESSOURCES HUMAINES ET RENFORCEMENT DES CAPACITÉS A CIVAS. Responsable suivi-Évaluations a HURDA." : "Étudiant",
                                             "Aucun" : "Sans emploi",
                                             "Étudiants" : "Étudiant",
                                             "Étudiant / Student" : "Étudiant",
                                             "Aucune" : "Sans emploi",
                                             "Étudiant chercheur" : "Étudiant",
                                             "Étudiant et Assistant de recherche" : "Étudiant",
                                             "Job-searching" : "Sans emploi",
                                             "Etudiant en pharmacie" : "Étudiant",
                                             "Chercheuse d'emploi" : "Sans emploi",
                                             "Pour le moment je ne travaille pas " : "Sans emploi",
                                             "etudiante" : "Sans emploi",
                                             "Aucun" : "Sans emploi",
                                             "Jobless" : "Sans emploi",
                                             "I'm still searching for a job" : "Sans emploi",
                                             "student" : "Étudiant",
                                             "Student" : "Étudiant",
                                             "None" : "Étudiant",
                                             "Nothing" : "Sans emploi",
                                             "Ras" : "Sans emploi",
                                             "Etudiante" : "Étudiant",
                                             "Étudiant/ Jeune entrepreneur" : "Étudiant",
                                             "Élève ingénieur à l'école nationale supérieure polytechnique de Maroua" : "Étudiant",
                                             "À mon propre compte" : "Entrepreneur",
                                             "Étudiants/ peintre" : "Étudiant",
                                             "ELEVE PROFESSEUR" : "Étudiant",
                                             "Étudiant et entrepreneur" : "Entrepreneur",
                                             "Sans emploi (étudiant)" : "Étudiant",
                                             "APPRENANT AU CENTRE DE FORMATION PROFESDIONNELLE" : "Étudiant",
                                             "ÉTUDIANT" : "Étudiant",
                                             "Suis étudiante" : "Étudiant",
                                             "Etudiant Gestion des resources humaine" : "Étudiant",
                                             "ÉTUDIANT-ENTREPRENEUR" : "Entrepreneur",
                                             "ÉTUDIANTE CHERCHEUR" : "Étudiant",
                                             "I’m a student" : "Étudiant",
                                             "Student." : "Étudiant",
                                             "Entrepreneur / Entrepreneur" : "Entrepreneur",
                                             "Professionnel en marketing / Marketing professional" : "Professionnel en marketing",
                                             "Journaliste / Journalist" : "Journaliste",
                                             "Personnel de santé / Healthcare personnel" : "Personnel de santé",
                                             "Avocat / Lawyer" : "Avocat",
                                             "Étudiant / Student" : "Étudiant",
                                             "Enseignant / Teacher" : "Enseignant",
                                             "Ingénieur qualité / Quality engineer" : "Ingénieur qualité",
                                             "Responsable ressources humaines / Human resources manager" : "Responsable ressources humaines",
                                             "Artiste / Artist" : "Artiste",
                                             "Ingénieur agricole / Agricultural engineer" : "Ingénieur agricole",
                                             "Sans emploi /" : "Sans emploi",
                                             "Administrative Assistant/Tutor" : "Administrative Assistant",
                                             "Actuellement je suis sans emploi" : "Sans emploi"
                                             
                                                    
                                                    })

df["pole"] = df['pole'].replace({"Équipe Exécutive / Executif team" : "Équipe Exécutive",
                                                     "Engagement/ Engagement" : "Engagement",
                                 "LaB/ LaB" : "LaB",
                                 "Overseas/ Overseas" : "Overseas",
                                 "Communication et Marketing/ Communication and Marketing" : "Communication et Marketing",
                                 "Stratégie et Organisation/ Strategy and Organisation" : "Stratégie et Organisation",
                                 "Finance, Partenariats et Administratif/ Finance, Partnerships and Administration" : "Finance, Partenariats et Administratif",
                                 "Labo FIDEMO/ Labo FIDEMO" : "Labo FIDEMO",
                                 "Hub/ Hub" : "Hub"  
                                                    })
                                       
df



# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()

# 4) Selectionner les données
Lauréat = df[df['membership'] == 'Lauréat.e/ Laureate']
Elders = df[df['membership'] == 'Ainé / Elder']
Partenaire = df[df['membership'] == 'Partenaire/ Partner']
Family = df[df['membership'] == 'Membre de la family/ Member of The Family']
Adhérent = df[df['membership'] == 'Membre adhérent "membre cotisant"/ Subscribing member "contributing member"']
Mentor= df[df['membership'] == 'Mentor/Formateur/Intervenant/Modérateur']
Autres= df[df['membership'] .isin(["Participant aux ateliers / workshop participants", "Je m'engage pour l'Afrique", "Non admis aux programmes (OFYCL, O'100)"])]

 #✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM lauréats")

#-- Vérifiez si l'email existe
for _, row in Lauréat.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM Lauréats WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO lauréats (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, programme, année_programme, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['programme'], row['année'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")



# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM membre_de_la_family")

#-- Vérifiez si l'email existe
for _, row in Family.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM membre_de_la_family WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO membre_de_la_family (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")


# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM membre_adhérents")

#-- Vérifiez si l'email existe
for _, row in Adhérent.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM membre_adhérents WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO membre_adhérents (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")



# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM partenaires")

#-- Vérifiez si l'email existe
for _, row in Partenaire.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM partenaires WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO partenaires (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")


# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM elders")

#-- Vérifiez si l'email existe
for _, row in Elders.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM elders WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO elders (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")


# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM autres")

#-- Vérifiez si l'email existe
for _, row in Autres.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM autres WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO autres (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année, membership) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'], row['membership'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")


# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM general")

#-- Vérifiez si l'email existe
for _, row in df.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM general WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO general (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année, membership, pole_benevolat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['Horodateur'], row['membership'], row['pole'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")



# ✅ 3) Connexion MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Annuaire",
  database="the_okwelians"
)
cursor = conn.cursor()


#✅ 4) Vider la table avant d'insérer (optionnel)
cursor.execute("DELETE FROM mentors")

#-- Vérifiez si l'email existe
for _, row in Mentor.iterrows():
    email = row['email']
    doublon_query = "SELECT COUNT(*) FROM mentors WHERE email = %s"
    cursor.execute(doublon_query, (email,))
    count = cursor.fetchone()[0]

    if count == 0 :

        sql = "INSERT INTO mentors (prénom, nom, téléphone1, téléphone2, email, sexe, age, diplôme, profession, structure, secteur, secteur_activité, pays_de_résidence, région_de_résidence, département_de_résidence, ville_de_résidence, région_origine, année_intervention, programme, année) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (row['prénom'], row['nom'], row['téléphone1'], row['téléphone2'], row['email'], row['sexe'], row['age'], row['diplome'], row['profession'], row['structure'], row['secteur'], row['secteur_activite'], row['pays_de_residence'], row['region_de_residence'], row['departement_de_residence'], row['ville_de_residence'], row['region_origine'], row['année_intervention'],row['programme_intervention'], row['Horodateur'])
        cursor.execute(sql, values)

    else : 

         print("l'email supprimé:", email)
         

conn.commit()

# ✅ 6) Fermer la connexion
cursor.close()
conn.close()

        


  
print("✅ Synchronisation terminée avec succès !")
