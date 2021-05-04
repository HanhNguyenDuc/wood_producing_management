from .views import *


# Form definition
class ChangePasswordForm(forms.Form):
    username = forms.CharField(max_length=100)
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        


# View definition
@login_required
def change_password(request):
    if request.method == "POST":
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
    else:
        form = ChangePasswordForm()
        context = {
            "form": form
        }
        return render(request, 'wood_producing/user_base/change_password.html', context)