from django.urls import path
from .  import views

app_name = 'search'
urlpatterns = [
    path('list/', views.SearchView.as_view(), name='results'),
    path('form/', views.SearchFormView.as_view(), name = 'formView'),

]
