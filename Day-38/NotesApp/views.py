from django.shortcuts import render
from .forms import UsForm

# Create your views here.

def home(request):
	return render(request,'notehtmls/home.html')

def about(request):
	return render(request,'notehtmls/about.html')

def contact(request):
	return render(request,'notehtmls/contact.html')

def register(request):
	u = UsForm()
	return render(request,'notehtmls/register.html',{'us':u})