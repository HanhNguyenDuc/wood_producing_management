from .views import *
from django.db import connection


class ProfitStatistic(RoleRequiredView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'wood_producing/statistic/profit.html')
        else:
            return HttpResponseRedirect(get_user_role_root_path(request.user))

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)

class ProductionStatistic(RoleRequiredView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'wood_producing/statistic/production.html')
        else:
            return HttpResponseRedirect(get_user_role_root_path(request.user))

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)


class MaterialStatistic(RoleRequiredView):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render(request, 'wood_producing/statistic/material.html')
        else:
            return HttpResponseRedirect(get_user_role_root_path(request.user))

    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)