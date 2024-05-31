from django.urls import path
from .views import send_reset_password_email, reset_password

urlpatterns = [
    path('send-reset-password-email/', send_reset_password_email, name='send_reset_password_email'),
    path('reset-password/', reset_password, name='reset_password'),
]

app_name = 'forgot_password'