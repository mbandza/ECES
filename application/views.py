from django.shortcuts import render
from .models import Etudiant
from django.views.generic import DetailView

def etudiant(request):
	etudiant=Etudiant.objects.all()
	return render(request,"pages/etudiant.html",{'etudiant':etudiant})
	
def acceuil(request):
	return render(request, "pages/acceuil.html")

def profils(request):
	voir=Etudiant.objects.get(pk=id)
	return render(request, "pages/profils.html",{'voir':voir})

class Profils(DetailView):
	model=Etudiant
	template_name="pages/profils.html"


