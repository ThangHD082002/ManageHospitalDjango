from django.urls import path
from .views import user_login, get_patient_list

urlpatterns = [
    path('login/', user_login, name='login'),
    path('list-patient/', get_patient_list, name='patient_list'),

]

app_name = 'login'