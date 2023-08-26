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
	pfimg = models.ImageField(upload_to='Profiles/',default='demoprofile.png')

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

class Notes(models.Model):
	y = [
		('0','Select Year'),
		('1','1st Year'),
		('2','2nd Year'),
		('3','3rd Year'),
		('4','4th Year'),
	]
	branch = models.CharField(max_length=50)
	year = models.CharField(default='0',choices=y,max_length=5)
	subject = models.CharField(max_length=50)
	descnote = models.CharField(max_length=10)
	ntfle = models.FileField(upload_to='DataFiles')
	date_created = models.DateField(auto_now=True)
	sckey = models.CharField(max_length=10)
	usr = models.ForeignKey(User,on_delete=models.CASCADE)


