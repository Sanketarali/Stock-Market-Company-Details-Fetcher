# stockapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company_details, name='company_details'),
]
