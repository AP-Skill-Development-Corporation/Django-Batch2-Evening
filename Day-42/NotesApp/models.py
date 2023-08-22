from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	v = [
		('d','Select Your gender'),
		('M','Male'),
		('F','Female'),
	]
	p = [
		('G','Guest'),
		('T','Teacher'),
		('S','Student'),
	]
	gd = models.CharField(choices=v,default='d',max_length=5)
	mb = models.CharField(max_length=11)
	uq = models.CharField(max_length=10)
	role = models.CharField(choices=p,default='G',max_length=5)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)

class TProfile(models.Model):
	branch = models.CharField(max_length=50)
	subjects = models.CharField(max_length=50)
	expr = models.IntegerField()
	designation = models.CharField(max_length=50)
	tch = models.OneToOneField(User,on_delete=models.CASCADE)

class SProfile(models.Model):
	y = [
		('0','Select Year'),
		('1','1st Year'),
		('2','2nd Year'),
		('3','3rd Year'),
		('4','4th Year'),
	]
	branch = models.CharField(max_length=50)
	year = models.CharField(default='0',choices=y,max_length=5)
	stdnt = models.OneToOneField(User,on_delete=models.CASCADE)

