from multiprocessing import context
from django.shortcuts import render
from myapp.models import *
from myapp.forms import *
# Create your views here.

def contact(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
    
  context = {'form': form}
    
  return render(request,'myapp/base.html', context)
  