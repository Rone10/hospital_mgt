from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DetailView,ListView,DeleteView
# Create your views here.

def index(request):
    return render(request, 'accounts/doctor_dashboard.html')

from django.views.generic.base import TemplateView

from .models import Doctor, Patient

class DocsPageView(TemplateView):

    template_name = "accounts/doc_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docs_list'] = Doctor.objects.all()
        docs = Doctor.objects.get(pk=2)
        context['docs_patients_list'] = docs.patient_set.all()
        context['patients'] = Patient.objects.all()
        return context

class AdminHomeView(TemplateView):
    template_name = "accounts/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['docs'] = Doctor.objects.all()
        context['patients_list'] = Patient.objects.all()
        return context

# views
class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'accounts/doc_detail.html'
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # doc_id = Doctor.objects.get(pk=self.request.user.id)
        # context['patients_list'] = doc_id.patient_set.all()
        doc_id =self.request.user.id
        context['ID']= doc_id
        return context