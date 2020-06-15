"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.urls import path
import os
from django.core.management import call_command

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("financial_GUI_package/", views.financial_GUI_package, name="financial_GUI_package"),
    path("dating_app/", views.dating_app, name="dating_app"),
    path("graphical_analysis_application/", views.graphical_analysis_application, name="graphical_analysis_application"),
    path("tennis_serve_simulator/", views.tennis_serve_simulator, name="tennis_serve_simulator"),
    path("thermal_analysis_simulation/", views.thermal_analysis_simulation, name="thermal_analysis_simulation"),
    path("financial_website_application/", views.financial_website_application, name="financial_website_application"),
    path("financial_GUI_package_2/", views.financial_GUI_package_2, name="financial_GUI_package_2"),
    path("website_chatbot/", views.website_chatbot, name="website_chatbot"),
    path("Food_tracking_web_app/", views.food_tracking_web_app, name="food_tracking_web_app"),
]

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




 