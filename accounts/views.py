from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView,DetailView,ListView,DeleteView, View
from . forms import UserCreateForm, PatientSignupForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .models import Doctor, Patient, User, Appointment
from django.contrib.auth.mixins import LoginRequiredMixin

class DocsPageView(ListView):
    model = Doctor
    template_name = "accounts/doc_list.html"
    context_object_name = 'docs'


class AdminHomeView(TemplateView):
    template_name = "accounts/admin_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['docs'] = Doctor.objects.all()
        # context['patients_list'] = Patient.objects.all()
        # return context
        if self.request.user.is_authenticated and not self.request.user.is_superuser:
            patient = Patient.objects.get(user=self.request.user)
            if patient:
                context['patient'] = patient
        # context = super().get_context_data(**kwargs)
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
            doc_id = Doctor.objects.get(id=self.kwargs['pk'])
            context['patients_list'] = doc_id.patient_set.all()
            return context
        return


class UserSignupView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('accounts:home')


class Homepage(TemplateView):
    template_name = 'accounts/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['docs'] = Doctor.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'accounts/about.html'


class ContactPageView(TemplateView):
    template_name = 'accounts/contact.html'


class BookingView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated :
            try:
                Patient.objects.get(user = self.request.user)
            except:
                return HttpResponseRedirect(reverse_lazy('account:patientform')) #send logged in user to patient signup form then redirect back to homepage/ booking page
            Appointment.objects.create(patient=self.request.user)
            return HttpResponseRedirect(reverse_lazy('account:confirmation'))
        return HttpResponseRedirect(reverse_lazy('login'))


class AppointmentBookedView(TemplateView):
    template_name = 'accounts/booked.html'


class PatientFormView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/patient_signup.html'
    form_class = PatientSignupForm
    context_object_name = 'form'
    success_url = reverse_lazy('accounts:home')

    def get_context_data(self, **kwargs):
        context= super().get_context_data()
        try:
            patient = Patient.objects.get(user=self.request.user)
            context[ 'patient' ] = patient
        except:
            context['patient'] = False

        # patient = Patient.objects.get(user=self.request.user)
        # if patient:

        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super().form_valid(form)
