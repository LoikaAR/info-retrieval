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
# from myapp.views import get_data  # Import the view
from myapp.views import get_csrf_token

urlpatterns = [
    # path('api/data/', get_data, name='get_data'),  # Map the view to a URL
    path('api/get_csrf_token/', get_csrf_token, name='get_csrf_token'),
    path('api/submit-form/', views.submit_form, name='submit_form'),  # Define the URL pattern
    path('', admin.site.urls),
]

