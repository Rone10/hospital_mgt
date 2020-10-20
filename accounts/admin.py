from django.contrib import admin
from . models import User, Doctor, Patient

# Register your models here.

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('email','first_name', 'last_name', 'username', )
    list_filter = ('username',)
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'email')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = ('doc_first_name','address', 'department')
    list_filter = ('department',)
    search_fields = ('department',)


@admin.register(Patient)
class DoctorAdmin(admin.ModelAdmin):

    list_display = ('patient_first_name','address', 'assigned_to')
    list_filter = ('date_admitted',)
    search_fields = ('user__first_name', 'department')



