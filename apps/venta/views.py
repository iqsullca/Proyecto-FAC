from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
from apps.venta.forms import ClienteForm
from apps.venta.models import Cliente



def index(request):
	return render(request,'venta/index.html')

class ClienteList(ListView):
	model = Cliente
	template_name = 'venta/cliente_list.html'

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'venta/cliente_form.html'
    success_url = reverse_lazy('venta:cliente_listar')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'venta/cliente_form.html'
    success_url = reverse_lazy('venta:cliente_listar')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'venta/cliente_delete.html'
    success_url = reverse_lazy('venta:cliente_listar')
    
