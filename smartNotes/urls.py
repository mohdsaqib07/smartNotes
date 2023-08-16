"""
URL configuration for smartNotes project.

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
from django.urls import path , include
from . import views

admin.site.site_header = 'smartNotes Administration'
admin.site.site_title = 'smartNotes'
admin.site.index_title = 'Saqib\'s Website Copyright @ All rights reserved'

handler404 = views.custom_404_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('smart/',include('notes.urls')),
    path('__debug__/',include('debug_toolbar.urls')),
]
