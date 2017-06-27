"""automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import automation_app.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', automation_app.views.index, name = 'index'),
    url(r'^quarto/', automation_app.views.quarto, name = 'quarto'),
    url(r'^sala/', automation_app.views.sala, name = 'sala'),
    url(r'^area_externa/', automation_app.views.area_externa, name = 'area_externa'),
    url(r'^open_socket/', automation_app.views.open_socket, name = 'open_socket'),


]
