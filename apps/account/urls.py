from .views import *
from django.urls import path


app_name = "account"
urlpatterns = [
    path("register/", register_account, name="register_account"),
    path("login/", login_account, name="login_account"),
    path("logout/", logout_account, name="logout_account"),
    path('activate/<uidb64>/<token>/',activate_account,name='activate_account'),
]
