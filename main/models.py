from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

class botModel(models.Model):

    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
    
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "bot"

    def __str__(self):
        return self.input
    
        
        