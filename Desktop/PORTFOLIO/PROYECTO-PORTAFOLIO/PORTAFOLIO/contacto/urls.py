from django.urls import path
from .import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('agradecimiento/', views.agradecimiento, name='agradecimiento'),  # Nombre definido aquí
]


