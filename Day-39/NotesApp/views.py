from django.shortcuts import render,redirect
from .forms import UsForm
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'notehtmls/home.html')

def about(request):
	return render(request,'notehtmls/about.html')

def contact(request):
	return render(request,'notehtmls/contact.html')

def register(request):
	if request.method == "POST":
		u = UsForm(request.POST)
		if u.is_valid():
			d=u.save(commit=False)
			messages.success(request,f"{d.username} User Created Successfully")
			d.save()
			return redirect('/reg')
	else:
		u = UsForm()
	return render(request,'notehtmls/register.html',{'us':u})