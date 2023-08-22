from django.shortcuts import render,redirect
from .forms import UsForm,Adrolech,TchPf
from django.contrib import messages
from .models import User

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
			return redirect('/login')
	else:
		u = UsForm()
	return render(request,'notehtmls/register.html',{'us':u})

def rolechange(request):
	k = User.objects.all()
	return render(request,'notehtmls/role.html',{'u':k})

def roleupdate(request,t):
	g = User.objects.get(id=t)
	if request.method == "POST":
		n = Adrolech(request.POST,instance=g)
		if n.is_valid():
			n.save()
			messages.success(request,"Role Updated Successfully")
			return redirect('/roles')
	n = Adrolech(instance=g)
	return render(request,'notehtmls/roleupdate.html',{'v':n})

def profile(request):
	return render(request,'notehtmls/profile.html')