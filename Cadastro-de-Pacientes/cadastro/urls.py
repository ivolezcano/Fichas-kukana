from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view responsável, nome de referência. 
    path('',views.home,name='home'),
    path('fichas/',views.trabajos, name='listagem_usuarios'),
]
