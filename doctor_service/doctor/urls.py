from django.urls import path

from . import views

urlpatterns = [
    path('get-doctor-by-id/<int:user_id>/', views.get_doctor_by_id, name='get_user_by_id'),
]

app_name = 'doctor'
