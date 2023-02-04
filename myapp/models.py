from email import message
from logging import PlaceHolder
from tkinter import Widget
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length = 200)
   email = models.EmailField()
   message = models.TextField(max_length= 500)
   
   def __str__(self):
     return self.name
   
   