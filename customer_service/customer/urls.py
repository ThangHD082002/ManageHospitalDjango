from django.urls import path
from . import views

urlpatterns = [
    path('get-customer-by-id/<int:user_id>/', views.get_customer_by_id, name='get_user_by_id'),
]

app_name = 'customer'
