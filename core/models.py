import os
from django.db import models
from django.utils.timezone import now


class Takmicenje(models.Model):	
	naziv = models.CharField(max_length=100, null=True, default=1)
class Trka(models.Model):	
	takmicenje = models.ForeignKey(Takmicenje, on_delete=models.CASCADE)
	naziv = models.CharField(max_length=100, null=True, default=1)
	duzina_km = models.IntegerField(max_length=15, null=True)
	cena = models.IntegerField(max_length=15, null=True)
	datum = models.DateTimeField(null=True, default=now)
	organizator = models.CharField(max_length=100, null=True, default=1)
class Takmicar(models.Model):	
	trka = models.ForeignKey(Trka, on_delete=models.CASCADE)
	ime = models.CharField(max_length=100, null=True, default=1)
	prezime = models.CharField(max_length=100, null=True, default=1)
	jmbg = models.CharField(max_length=100, null=True, default=1)
	pol = models.CharField(max_length=13, null=True, default=1)
	kontakt = models.EmailField(max_length=64, null=False, default=1)