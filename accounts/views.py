from django.views.generic import CreateView, UpdateView,DetailView,ListView,DeleteView
from . forms import UserCreateForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Doctor, Patient, User


class DocsPageView(TemplateView):

    template_name = "accounts/doc_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['docs_list'] = Doctor.objects.all()
        doc = Doctor.objects.get(user=self.request.user)
        context['docs_patients_list'] = doc.patient_set.all()
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
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            doc_id = Doctor.objects.get(user=self.request.user)
            context['patients_list'] = doc_id.patient_set.all()
            doc_id =self.request.user.first_name
            context['ID']= doc_id
            return context
        return


class UserSignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('login')
