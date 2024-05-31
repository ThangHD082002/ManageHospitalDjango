from django.urls import path
from .views import add_appointment,add_phong, get_appointment_by_id, get_appointments_by_doctor_id, get_all_appointments

urlpatterns = [
    path('add-appointment/', add_appointment, name='add_appointment'),
    path('add-phong/', add_phong, name='add_appointment'),
    path('get-appointment-by-id/<int:id>/', get_appointment_by_id, name='get_appointment_by_id'),
    path('get-appointments-by-doctor-id/<int:doctor_id>/', get_appointments_by_doctor_id, name='get_appointments_by_doctor_id'),
    path('get-all-appointments/', get_all_appointments, name='get_appointments_by_doctor_id'),
]


app_name = 'appointment'