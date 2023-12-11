"""
URL configuration for myproject project.

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
from myapp import views
from myapp.views import get_csrf_token
from myapp.views import get_data
from myapp.views import get_regions
from myapp.views import get_categories

urlpatterns = [
    path('api/get_csrf_token/', get_csrf_token, name='get_csrf_token'),
    path('api/get_data/', get_data, name='get_data'),
    path('api/get_regions/', get_regions, name='get_regions'),
    path('api/get_categories/', get_categories, name='get_categories'),
    path('api/submit_recommendation/', views.submit_recommendation, name='submit_recommendation'),
    path('api/submit-form/', views.submit_form, name='submit_form'),
    path('', admin.site.urls)
]
