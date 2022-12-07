from django.urls import path
from .views import home,lista,galeria,contacto

urlpatterns = [
    path('', home, name="home"),
    path('lista-talleres/', lista,name="lista de talleres"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
]