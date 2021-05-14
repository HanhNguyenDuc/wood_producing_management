from .views import *

class MainProducingManagerView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "wood_producing/producing_manager/orders.html"

    direct_url = {
        "order_detail": "producing_manager/order_detail",
        "change_password": "user/change_password",
        "logout": "user/logout",
    }

    def update_get_context(self, request, *args, **kwargs):
        search_query = request.GET.get("order_name")
        customer_id = request.GET.get("customer_id")
        page_size = settings.PAGE_SIZE
        page_num = request.GET.get("page_num")
        orders = Order.objects.all()
        if search_query is not None:
            orders = orders.filter(name__contains=search_query)
        if customer_id is not None:
            orders = orders.filter(customer__id=customer_id)
        for order in orders:
            task_num = 0
            task_done = 0
            ordered_products = Orderedproduct.objects.filter(order=order)
            for ordered_product in ordered_products:
                task_num += Task.objects.filter(orderedproductid=ordered_product).count()
                task_done += Task.objects.filter(orderedproductid=ordered_product, progress__id=1).count()
            setattr(order, 'total_task_num', task_num)
            setattr(order, 'done_task_num', task_done)


        p = Paginator(orders, page_size)
        cur_page = p.page(1)
        if page_num is not None:
            cur_page = p.page(page_num)
        
        self.context["num_pages"] = p.num_pages
        self.context["pages"] = range(1, p.num_pages+1)
        self.context["orders"] = cur_page.object_list
        return None
    
    def update_post_context(self, request, *args, **kwargs):
        return None


class ManageTaskView(RoleRequiredView):
    user_role = 1
    form = None
    template_path = "wood_producing/producing_manager/order_detail.html"

    direct_url = {
        "main_producing_manager": "/producing_manager",
        "logout": "user/logout",
        "change_password": "user/change_password",
        "add_task": "user/add_task",
    }

    def update_get_context(self, request, *args, **kwargs):
        pk = kwargs['order_id']
        order = Order.objects.get(id=pk)
        ordered_products = Orderedproduct.objects.filter(order=order)
        for ordered_product in ordered_products:
            tasks = Task.objects.filter(orderedproductid=ordered_product)
            setattr(ordered_product, 'tasks', tasks)
            assigned_product = 0
            for task in tasks:
                assigned_product += task.quantity
            setattr(ordered_product, 'assigned_product', assigned_product)

        self.context['order'] = order
        self.context['ordered_products'] = ordered_products
        return None
    
    def update_post_context(self, request, *args, **kwargs):
        return None