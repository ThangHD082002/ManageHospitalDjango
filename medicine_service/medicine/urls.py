from django.urls import path
from . import views

urlpatterns = [
    path('add-producer/', views.add_producer, name='add_producer'),
    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('add-patient-medicine/', views.add_patient_medicine, name='add_patient_medicine'),
    path('add-item-patient-medicine/', views.add_item_patient_medicine, name='add_item_patient_medicine'),
    path('get-all-producers/', views.get_all_producers, name='get_all_producers'),
    path('get-all-medicines/', views.get_all_medicines, name='get_all_medicines'),
    path('get-all-patient-medicines/', views.get_all_patient_medicines, name='get_all_patient_medicines'),
    path('get-all-item-patient-medicines/', views.get_all_item_patient_medicines, name='get_all_item_patient_medicines'),
    path('get-item-patient-medicines/<int:patient_medicine_id>/', views.get_item_patient_medicines_by_patient_id, name='get_item_patient_medicines_by_patient_id'), 
    path('update-item-patient-medicine/<int:item_id>/', views.update_item_patient_medicine, name='update_item_patient_medicine'),
    path('delete-item-patient-medicine/<int:item_id>/', views.delete_item_patient_medicine, name='delete_item_patient_medicine'),
]

app_name = 'medicine'