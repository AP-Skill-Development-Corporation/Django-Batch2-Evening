# from django.contrib.auth.models import User
from NotesApp.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","uq"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Roll Number/Employee ID",
			}),
		}

class Adrolech(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","uq","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
		