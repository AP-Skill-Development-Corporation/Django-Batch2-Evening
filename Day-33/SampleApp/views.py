from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Hello guys welcome to django internship</h1>")


def sam(request):
	return HttpResponse("<h2 style=color:green;background-color:yellow;font-size:45px><center>Django Internship</center></h2>")

def dynamic(request,id):
	return HttpResponse("<h2><center>My Rollnumber is:{}</center></h2>".format(id))

def data(request,name):
	return HttpResponse("<h1 style=color:navy;background-color:green;font-style:italic><center>My Name is :{}</center></h1>".format(name))

def task(request,a,b):
	return HttpResponse("<h2><center>my rollnumber is:{} and my name is:{}</center></h2>".format(a,b))


def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html',{})


def det(request,id,name):
	return render(request,'details.html',{'i':id,'n':name})

def inline(request):
	return render(request,'inline.html',{})


def internal(request):
	return render(request,'internal.html')

def external(request):
	if request.method=="POST":
		na=request.POST['uname']
		mb=request.POST['mbl']
		em=request.POST['eml']
		ps=request.POST['psw']
		cps=request.POST['cpsw']
		# print(na,mb,em,ps,cps)
		return render(request,'data.html',{'n':na,'m':mb,'e':em,'p':ps,'cp':cps})

	return render(request,'external.html')

def boot(request):
	return render(request,'boot.html')

def btp(request):
	return render(request,'bt/home.html')

def crud(request):
	return render(request,'bt/crudoperations.html')