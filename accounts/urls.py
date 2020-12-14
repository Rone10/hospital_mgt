from django.urls import path
from .  import views

app_name = 'account'
urlpatterns = [
    path('list/', views.DocsPageView.as_view(), name='docs'),
    path('adminhome/', views.AdminHomeView.as_view(), name='adminhome'),
    path('detail/<int:pk>/', views.DoctorDetailView.as_view(), name='detail'),
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('home/', views.Homepage.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('patientform/', views.PatientFormView.as_view(), name='patientform'),
    path('confirmation/', views.AppointmentBookedView.as_view(), name='confirmation'),
]
