from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/change_password',views.change_password, name="change_password"),
    path('user/login', auth_views.LoginView.as_view(template_name="wood_producing/user_base/login.html"), name="login"),
    path('user/logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]