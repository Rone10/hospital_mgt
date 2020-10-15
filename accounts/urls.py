from django.urls import path
from .  import views

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index' ),
    path('list/', views.DocsPageView.as_view(), name='docs'),
    path('home/', views.AdminHomeView.as_view(), name='home'),
    path('detail/<int:pk>/', views.DoctorDetailView.as_view(), name='detail'),
]
