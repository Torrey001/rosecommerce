from django.urls import path
from .views import create_user, getUser, update_user, delete_user

urlpatterns = [
    # getUser
    path('get_user/', getUser, name="get_user"),
    path('create_user/', create_user, name="create_user"),
    path('update_user/<int:pk>/', update_user, name='update_user'),
    path('delete_user/<int:pk>/', delete_user, name='delete_user')
]