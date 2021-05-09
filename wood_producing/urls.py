from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/change_password',views.ChangePasswordView.as_view(), name="change_password"),
    path('user/login', auth_views.LoginView.as_view(template_name="wood_producing/user_base/login.html"), name="login"),
    path('user/logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    path('producing_manager', views.MainProducingManagerView.as_view()),
    path('', views.Index.as_view(), name='index')
]