from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp.forms import CustomAuthForm
from myapp import views


urlpatterns = [
    path("", include("myapp.urls")),
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("accounts/update/", views.change_password, name="profile_update"),
]
