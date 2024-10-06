# api/urls.py
from django.urls import path
from .views import client_project_view, edit_client, delete_client, edit_project, delete_project

urlpatterns = [
    path('', client_project_view, name='client_project'),
    path('edit_client/<int:client_id>/', edit_client, name='edit_client'),
    path('delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('edit_project/<int:project_id>/', edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
    # path('register/', register, name='register'),  # Registration URL
]
