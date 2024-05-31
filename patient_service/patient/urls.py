from django.urls import path
from . import views

urlpatterns = [
    path('add-patient/', views.add_patient, name='add_patient'),
    path('update-patient/<int:id>/', views.update_patient, name='update_patient_by_customer_id'),
    path('get-patient/<int:customer_id>/', views.get_patients_by_customer_id, name='get_patient_by_customer_id'),
    path('delete-patient/<int:patient_id>/', views.delete_patient_by_id, name='delete_patient_by_customer_id'),
    path('get-patient-by-id/<int:id>/', views.get_patient_by_id, name='delete_patient_by_customer_id'),
]


app_name = 'patient'