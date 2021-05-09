from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.views import View
from django import forms

from ..models import *

class RoleRequiredView(View):
    user_role = None
    form = None
    template_path = ""

    error_messages = {

    }
    """
        View for Role Required
    """
    def role_required_decorator(func):
        def _wrapped_view(self, request, *args, **kwargs):
            try:
                if self.user_role is None:
                    return JsonResponse({
                        "status": "Error",
                        "msg": "This view can't be access by Anonymous user",
                    })
                else:
                    if request.user.role != self.user_role:
                        return JsonResponse({
                            "status": "Error",
                            "msg": "This view can't be access by this user"
                        })
                    
                    return func(self, request, *args, **kwargs)
            except Exception as e:
                return JsonResponse({
                    "status": "Error",
                    "msg": str(e),
                })
        return _wrapped_view

    def update_get_context(self, request, *args, **kwargs):
        """
            main content define here
        """
        return None

    def update_post_context(self, request, *args, **kwargs):
        """
            main content define here
        """
        return None

    @method_decorator(login_required)
    @role_required_decorator
    def get(self, request, *args, **kwargs):
        """
            Default get processing
        """
        self.context = {}
        self.context["user"] = request.user
        if self.form is None:
            return render(request, self.template_path, self.context)
        
        form = self.form()
        self.context["form"] = form
        self.update_get_context(request, *args, **kwargs)

        return render(request, self.template_path, self.context)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """
            Default post processing
        """
        form = self.form(request.POST)
        self.context = {
            "form": form,
        }

        if form.is_valid():
            self.update_post_context(request, *args, **kwargs)
            return render(request, self.template_path, self.context)

