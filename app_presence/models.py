from django.db import models

# Create your models here.
class Grade (models.Model):
    codegrade = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100, null=False)

class  Fonction (models.Model):
    codefonction = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100, null=False)


class Direction (models.Model):
    codedirection = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100, null=False)
    
class Presence(models.Model):
    numpres = models.CharField(max_length=10, primary_key=True)
    datepres = models.DateTimeField()

class Agent (models.Model):
    numagent = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=100, null=False)
    postnom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, null=False)
    grade = models.ForeignKey(Grade, on_delete = models.DO_NOTHING)
    fonction = models.ForeignKey(Fonction, on_delete = models.DO_NOTHING)
    direction = models.ForeignKey(Direction, on_delete = models.DO_NOTHING)

class Carte (models.Model):
    codecarte = models.CharField(max_length=10, primary_key=True)
    anneeobtention = models.CharField(max_length=100, null=False)
    anneeexpiration = models.CharField(max_length=100, null=False)
    agent = models.ForeignKey(Agent, on_delete = models.DO_NOTHING)

class Prestation (models.Model):
    codeprestation = models.CharField(max_length=10, primary_key=True)
    heurearrive = models.TimeField()
    heuredepart = models.TimeField()
    agent = models.ForeignKey(Agent, on_delete = models.DO_NOTHING)
    presence = models.ForeignKey(Presence, on_delete = models.DO_NOTHING)

