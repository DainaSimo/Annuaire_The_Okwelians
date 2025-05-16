# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autres(models.Model):
    id_autre = models.AutoField(db_column='ID_Autre', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    membership = models.CharField(db_column='Membership', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autres'


class Bénévoles(models.Model):
    id_bénévole = models.AutoField(db_column='ID_Bénévole', primary_key=True)  # Field name made lowercase.
    pole = models.CharField(db_column='Pole', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lauréat = models.ForeignKey('Lauréats', models.DO_NOTHING, db_column='Lauréat', blank=True, null=True)  # Field name made lowercase.
    membre_adhérents = models.ForeignKey('Membre_Adhrents', models.DO_NOTHING, db_column='Membre_Adhérents', blank=True, null=True)  # Field name made lowercase.
    membre_de_la_family = models.ForeignKey('Membre_De_La_Family', models.DO_NOTHING, db_column='Membre_de_la_Family', blank=True, null=True)  # Field name made lowercase.
    autres = models.ForeignKey(Autres, models.DO_NOTHING, db_column='Autres', blank=True, null=True)  # Field name made lowercase.
    partenaires = models.ForeignKey('Partenaires', models.DO_NOTHING, db_column='Partenaires', blank=True, null=True)  # Field name made lowercase.
    mentors = models.ForeignKey('Mentors', models.DO_NOTHING, db_column='Mentors', blank=True, null=True)  # Field name made lowercase.
    elders = models.ForeignKey('Elders', models.DO_NOTHING, db_column='Elders', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bénévoles'


class Elders(models.Model):
    id_elder = models.AutoField(db_column='ID_Elder', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'elders'


class General(models.Model):
    id_général = models.AutoField(db_column='ID_General', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dÚpartement_de_rÚsidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'general'


class Laurats(models.Model):
    id_lauréat = models.AutoField(db_column='ID_Lauréat', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    programme = models.CharField(db_column='Programme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    année = models.CharField(db_column='Année_programme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lauréats'


class MembreAdhrents(models.Model):
    id_membre = models.AutoField(db_column='ID_Membre', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tÚlÚphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membre_adhérents'


class MembreDeLaFamily(models.Model):
    id_family = models.AutoField(db_column='ID_Family', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membre_de_la_family'


class Mentors(models.Model):
    id_mentor = models.AutoField(db_column='ID_Mentor', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    année = models.CharField(db_column='Année_intervention', max_length=100, blank=True, null=True)  # Field name made lowercase.
    programme = models.CharField(db_column='Programme', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qualité_intervention = models.CharField(db_column='Qualité_Intervention', max_length=100, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mentors'


class Partenaires(models.Model):
    id_partenaire = models.AutoField(db_column='ID_Partenaire', primary_key=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone1 = models.CharField(db_column='Téléphone1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    téléphone2 = models.CharField(db_column='Téléphone2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    diplôme = models.CharField(db_column='Diplôme', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=500, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=500, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=500, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='Structure', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur = models.CharField(db_column='Secteur', max_length=500, blank=True, null=True)  # Field name made lowercase.
    secteur_activité = models.CharField(db_column='Secteur_activité', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pays_de_résidence = models.CharField(db_column='Pays_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_de_résidence = models.CharField(db_column='Région_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    département_de_résidence = models.CharField(db_column='Département_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ville_de_résidence = models.CharField(db_column='Ville_de_résidence', max_length=500, blank=True, null=True)  # Field name made lowercase.
    région_origine = models.CharField(db_column='Région_origine', max_length=500, blank=True, null=True)  # Field name made lowercase.
    annéecourante = models.CharField(db_column='Année', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'partenaires'


class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    prénom = models.CharField(db_column='Prénom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
