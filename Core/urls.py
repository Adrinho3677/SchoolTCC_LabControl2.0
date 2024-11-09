"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ControleLab.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('acesso/', acesso, name='acesso'),
    path('adicionar_lab/', adicionar_lab, name='adicionar_lab'),
    path('computadores/<int:id>', computadores, name='computadores'),
    path('adicionar_comp/<int:id>', adicionar_comp, name='adicionar_comp'),
    path('alterar_status_comp/<int:id>', alterar_status_comp, name='alterar_status_comp'),
    path('excluir_comp/<int:id>', excluir_comp, name='excluir_comp'),
    path('relatorio', relatorio, name='relatorio'),
    path('criar_relatorio/<int:id>', criar_relatorio, name='criar_relatorio'),
    path('devolver_comp/<int:id>', devolver_comp, name='devolver_comp'),
    path('sair/', sair, name='sair'),
]
