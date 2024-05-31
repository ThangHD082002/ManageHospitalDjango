from django.urls import path
from . import views

urlpatterns = [
    path('add-producer/', views.add_producer, name='add_producer'),
    path('add-supply/', views.add_supply, name='add_supply'),
    path('add-patient-supply/', views.add_patient_supply, name='add_patient_supply'),
    path('add-item-patient-supply/', views.add_item_patient_supply, name='add_item_patient_supply'),
    path('get-all-producers/', views.get_all_producers, name='get_all_producers'),
    path('get-all-supplies/', views.get_all_supplies, name='get_all_supplies'),
    path('get-all-patient-supplies/', views.get_all_patient_supplies, name='get_all_patient_supplies'),
    path('get-all-item-patient-supplies/', views.get_all_item_patient_supplies, name='get_all_item_patient_supplies'),
    path('get-item-patient-supplies/<int:patient_supply_id>/', views.get_item_patient_supplies_by_patient_id, name='get_item_patient_supplies_by_patient_id'),
    path('update-item-patient-supply/<int:item_id>/', views.update_item_patient_supply, name='update_item_patient_supply'),
    path('delete-item-patient-supply/<int:item_id>/', views.delete_item_patient_supply, name='delete_item_patient_supply'),
]


app_name = 'supply'