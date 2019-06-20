from django.db import models

# Create your models here.
class Etudiant(models.Model):
	nom=models.CharField(max_length=30)
	prenom=models.CharField(max_length=30)
	matricule=models.CharField(max_length=20)
	adresse=models.CharField(max_length=100)
	option=models.CharField(max_length=100)
	niveau=models.CharField(max_length=20)
	description=models.TextField()
	photo=models.ImageField()
	
	def __str__(self):
		return self.nom.title()
		return self.prenom.title()