from django.db import models

# Create your models here.

class EmployeeData(models.Model):
	eid = models.CharField(max_length=10)
	ename = models.CharField(max_length=50)
	edesg = models.CharField(max_length=150)
	eage = models.IntegerField(default=25)

	
