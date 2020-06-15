from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import pandas as pd
from django.views.generic import TemplateView
import json
from datetime import date
import os
from .python.chatbot.main import chat
from .forms import botForm

# Create your views here.
def homepage(request):

    return render(request, 
                  'main/kirchel_adam_portfolio.html')
                  
def financial_GUI_package(request):

    return render(request=request,
                  template_name='main/financial_GUI_package.html')

def dating_app(request):

    return render(request=request,
                  template_name='main/dating_app.html')

def graphical_analysis_application(request):

    return render(request=request,
                  template_name='main/graph_extractor.html')

def tennis_serve_simulator(request):

    return render(request=request,
                  template_name='main/tennis_serve_simulator.html')

def thermal_analysis_simulation(request):

    return render(request=request,
                  template_name='main/spacecraft_tile_simulator.html')

def financial_website_application(request):

    return render(request=request,
                  template_name='main/financial_website.html')

def financial_GUI_package_2(request):

    return render(request=request,
                  template_name='main/financial_GUI_package_vol2.html')
                  
def website_chatbot(request):

    return render(request=request,
                  template_name='main/website_chatbot.html')
                  
def food_tracking_web_app(request):

    return render(request=request,
                  template_name='main/Food_tracking_web_app.html')
