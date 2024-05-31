from django.urls import path
from . import views

urlpatterns = [
    path('add-examination/', views.add_examination, name='add_examination'),
    path('add-patient-examination/', views.add_patient_examination, name='add_patient_examination'),
    path('add-item-patient-examination/', views.add_item_patient_examination, name='add_item_patient_examination'),
    path('get-all-examinations/', views.get_all_examinations, name='get_all_examinations'),
    path('get-all-patient-examinations/', views.get_all_patient_examinations, name='get_all_patient_examinations'),
    path('get-all-item-patient-examinations/', views.get_all_item_patient_examinations, name='get_all_item_patient_examinations'),
    path('get-item-patient-examinations/<int:patient_examination_id>/', views.get_item_patient_examinations_by_patient_id, name='get_item_patient_examinations_by_patient_id'),
    path('update-item-patient-examination/<int:item_id>/', views.update_item_patient_examination, name='update_item_patient_examination'),
    path('delete-item-patient-examination/<int:item_id>/', views.delete_item_patient_examination, name='delete_item_patient_examination'),
]

app_name = 'examination'