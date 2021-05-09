from .views import *


# Form definition
class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)


class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm()
        context = {
            "form": form
        }
        return render(request, 'wood_producing/user_base/change_password.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            if user == None:
                context["status"] = "notexist"
                return render(request, 'wood_producing/user_base/change_password.html', context)
            else:
                context["status"] = "success"
                user.set_password(form.cleaned_data.get('new_password'))
                user.save()
                return render(request, 'wood_producing/user_base/change_password.html', context)

class Index(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, 'wood_producing/user_base/index.html')