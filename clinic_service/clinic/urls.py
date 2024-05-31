from django.urls import path
from . import views

urlpatterns = [
    path('add-type-clinic/', views.add_type_clinic, name='add_type_clinic'),
    path('add-clinic/', views.add_clinic, name='add_clinic'),
    path('add-bed/', views.add_bed, name='add_bed'),
    path('get-bed-by-clinic-id/<int:clinic_id>/', views.get_bed_by_clinic_id, name='get_bed_by_clinic_id'),
    path('get-bed-by-id/<int:id>/', views.get_bed_by_id, name='get_bed_by_id'),
    path('get-clinics-by-type-clinic-id/<int:type_clinic_id>/', views.get_clinic_by_typeclinic_id, name='get_clinic_by_typeclinic_id'),
    path('get-room-by-id/<int:id>/', views.get_clinic_by_id, name='get_clinic_by_id'),
    path('get-type-room-by-id/<int:id>/', views.get_type_clinic_by_id, name='get_clinic_by_id'),
    path('get-all-type-clinics/', views.get_all_type_clinics, name='get_all_type_clinics'),
    path('get-all-clinics/', views.get_all_clinics, name='get_all_clinics'),
    path('get-all-beds/', views.get_all_beds, name='get_all_beds'),
]


app_name = 'clinic'