from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Takmicenje
from .models import Trka
from .models import Takmicar

class TakmicenjeCreateView(CreateView):
	template_name='.html'
	model=Takmicenje
	fields = ['naziv']
	success_url=reverse_lazy('')


class TakmicenjeUpdateView(UpdateView):
	template_name='.html'
	model=Takmicenje
	fields = ['naziv']


class TakmicenjeDeleteView(DeleteView):
	template_name='.html'
	model=Takmicenje
	success_url=reverse_lazy('')


class TakmicenjeListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Takmicenje'
	def get_queryset(self):
		return Takmicenje.object.all


class TrkaCreateView(CreateView):
	template_name='.html'
	model=Trka
	fields = ['takmicenje', 'naziv', 'duzina_km', 'cena', 'datum', 'organizator']
	success_url=reverse_lazy('')


class TrkaUpdateView(UpdateView):
	template_name='.html'
	model=Trka
	fields = ['takmicenje', 'naziv', 'duzina_km', 'cena', 'datum', 'organizator']


class TrkaDeleteView(DeleteView):
	template_name='.html'
	model=Trka
	success_url=reverse_lazy('')


class TrkaListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Trka'
	def get_queryset(self):
		return Trka.object.all


class TakmicarCreateView(CreateView):
	template_name='.html'
	model=Takmicar
	fields = ['trka', 'ime', 'prezime', 'jmbg', 'pol', 'kontakt']
	success_url=reverse_lazy('')


class TakmicarUpdateView(UpdateView):
	template_name='.html'
	model=Takmicar
	fields = ['trka', 'ime', 'prezime', 'jmbg', 'pol', 'kontakt']


class TakmicarDeleteView(DeleteView):
	template_name='.html'
	model=Takmicar
	success_url=reverse_lazy('')


class TakmicarListView(generic.ListView):
	template_name = '.html'
	context_object_name = 'all_Takmicar'
	def get_queryset(self):
		return Takmicar.object.all

