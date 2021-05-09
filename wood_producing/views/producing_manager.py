from .views import *

class MainProducingManagerView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "wood_producing/producing_manager/main_producing_manager.html"

    direct_url = {
        "manage_task": "producing_manager/manage_task",
        "progress_statistic": "producing_manager/progress_statistic",
        "change_password": "user/change_password",
        "logout": "user/logout",
    }

    def update_get_context(self, request, *args, **kwargs):
        return None


class ManageTaskView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "wood_producing/producing_manager/manage_task_view.html"

    direct_url = {
        "main_producing_manager": "/producing_manager",
        "logout": "user/logout",
        "change_password": "user/change_password",
        "add_task": "user/add_task",
    }

    def update_get_context(self, request, *args, **kwargs):
        search_query = request.GET.get("order_name")
        customer_id = request.GET.get("customer_id")
        orders = Order.objects.all()    
        if search_query is not None:
            orders = orders.filter(name__contains=search_query)
        if customer_id is not None:
            orders = orders.filter(customer__id=customer_id)
        self.context["orders"] = orders
        return None
    
    def update_post_context(self, request, *args, **kwargs):
        return None