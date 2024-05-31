from django.urls import path
from .views import delete_user, update_user, get_user_by_id

urlpatterns = [
    # Các URL khác của bạn
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('get_user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
]

app_name = 'info'