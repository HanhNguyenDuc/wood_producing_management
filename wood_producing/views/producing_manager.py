from .views import *

class MainProducingManagerView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "wood_producing/producing_manager/main_producing_manager.html"

    def update_get_context(self, request, *args, **kwargs):
        return None