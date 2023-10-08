from django.urls import path
from .views import index, contact, signup
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("signup/", view=signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html", authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]