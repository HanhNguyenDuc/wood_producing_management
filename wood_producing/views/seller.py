from .views import *
import logging

class ListOrder(RoleRequiredView):
    user_role = 5
    form = None
    template_path = "wood_producing/seller/list_order.html"
    direct_url = {
        "order_detail": "seller/order_detail",
        "change_password": "user/change_password",
        "logout": "user/logout",
    }
    def update_get_context(self, request, *args, **kwargs):
        search_query = request.GET.get("order_name")
        customer_id = request.GET.get("customer_id")
        page_size = settings.PAGE_SIZE
        page_num = request.GET.get("page_num")
        user_id = request.user.id
        orders = Order.objects.all().filter(userid=user_id)
        for x in orders:
            print(x)
        p = Paginator(orders, page_size)
        cur_page = p.page(1)
        if page_num is not None:
            cur_page = p.page(page_num)
        self.context["num_pages"] = p.num_pages
        self.context["pages"] = range(1, p.num_pages+1)
        self.context["orders"] = cur_page.object_list
        return None

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

class OrderDetail(RoleRequiredView):
    user_role = 5
    form = None
    template_path = "wood_producing/seller/order_detail.html"
    def update_get_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

class ListOrder(RoleRequiredView):
    user_role = 5
    form = None
    template_path = "wood_producing/foreman/foreman_main_view.html"
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
        return super().update_post_context(request, *args, **kwargs)
class CreateOrder(RoleRequiredView):
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

class PublishOrder(RoleRequiredView):
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)
    
    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)