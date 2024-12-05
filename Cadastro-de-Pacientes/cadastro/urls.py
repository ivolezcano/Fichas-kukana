from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view responsável, nome de referência. 
    path('',views.home,name='home'),
    path('fichas/',views.trabajos, name='listagem_usuarios'),
    path('fichas/<int:numero_trabajo>/', views.detalle_trabajo, name='detalle_trabajo'),
    path('fichas/<int:numero_trabajo>/descargar/', views.descargar_pdf, name='descargar_pdf'),
]
