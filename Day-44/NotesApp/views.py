from django.shortcuts import render,redirect
from .forms import UsForm,Adrolech,TchPf,UsupForm,StForm
from django.contrib import messages
from .models import User,TProfile,SProfile

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

def updateprofile(request):
	h = User.objects.get(id=request.user.id)
	d = []
	if h.role == 'T':
		c = TProfile.objects.filter(tch_id=request.user.id)
		for i in c:
			d.append(i.tch_id)
		if request.user.id not in d:
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				s = TchPf(request.POST)
				if v.is_valid() and s.is_valid():
					n = v.save(commit=False)
					n.is_teacher = 1
					n.save()
					r = s.save(commit=False)
					r.tch_id = request.user.id
					r.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			s = TchPf()
			return render(request,'notehtmls/upprofile.html',{'y':v,'n':s})
		else:
			f = TProfile.objects.get(tch_id=request.user.id)
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				s = TchPf(request.POST,instance=f)
				if v.is_valid() and s.is_valid():
					v.save()
					s.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			s = TchPf(instance=f)
			return render(request,'notehtmls/upprofile.html',{'y':v,'n':s})
	elif h.role == 'S':
		x = SProfile.objects.filter(stdnt_id=request.user.id)
		u = []
		for i in x:
			u.append(i.stdnt_id)
		if request.user.id not in u:
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				g = StForm(request.POST)
				if v.is_valid() and g.is_valid():
					a = v.save(commit=False)
					a.is_student = 1
					a.save()
					e = g.save(commit=False)
					e.stdnt_id=request.user.id
					e.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			g = StForm()
			return render(request,'notehtmls/upprofile.html',{'y':v,'d':g})
		else:
			q = SProfile.objects.get(stdnt_id=request.user.id)
			if request.method == "POST":
				v = UsupForm(request.POST,request.FILES,instance=h)
				g = StForm(request.POST,instance=q)
				if v.is_valid() and g.is_valid():
					v.save()
					g.save()
					return redirect('/pfle')
			v = UsupForm(instance=h)
			g = StForm(instance=q)
			return render(request,'notehtmls/upprofile.html',{'y':v,'d':g})
	else:
		pass