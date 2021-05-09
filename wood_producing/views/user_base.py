from .views import *
from django.contrib.auth import views as auth_views


# Form definition
class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class ChangePasswordView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm()
        context = {
            "form": form
        }
        return render(request, 'wood_producing/user_base/change_password.html', context)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = request.user
            if user == None:
                context["status"] = "notexist"
                return render(request, 'wood_producing/user_base/change_password.html', context)
            else:
                context["status"] = "success"
                new_password = form.cleaned_data.get('password')
                user.set_password(new_password)
                user.save()
                return render(request, 'wood_producing/user_base/change_password.html', context)

class Index(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return render(request, 'wood_producing/user_base/index.html')
        else:
            return HttpResponseRedirect(get_user_role_root_path(request.user))


class LoginView(auth_views.LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_redirect_url(self):
        """ Overrided """

        if self.request.method != "POST":
            return super().get_redirect_url()
        if not self.request.user.is_authenticated:
            return super().get_redirect_url()

        return get_user_role_root_path(self.request.user)