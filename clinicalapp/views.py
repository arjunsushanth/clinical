from django.shortcuts import render
from clinicalapp.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class PatientListView(ListView):
    model = Patient
    template_name ='patientlist.html'


class PatientCreateView(CreateView):
    model = Patient
    template_name = 'createpatient.html'
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'createpatient.html'
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "delete.html"
    success_url = reverse_lazy('index')




# Create your views here.
