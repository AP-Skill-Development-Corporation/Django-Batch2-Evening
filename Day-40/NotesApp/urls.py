from django.urls import path
from NotesApp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('login/',v.LoginView.as_view(template_name="notehtmls/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="notehtmls/logout.html"),name="lgo"),
]