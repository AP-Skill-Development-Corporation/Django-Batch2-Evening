from .models import EmployeeData
from django import forms

class Eform(forms.ModelForm):
	class Meta:
		model = EmployeeData
		fields = ["eid","ename","edesg","eage"]
		widgets = {
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Name",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Id",
			}),
		"edesg":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Employee Designation",
			}),
		"eage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"min":20,
			"max":50,
			}),
		}