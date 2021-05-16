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
        order_id = kwargs['order_id']
        order = Order.objects.get(id=order_id)
        ordered_products = Orderedproduct.objects.filter(order=order)
        for ordered_product in ordered_products:
            total_price = ordered_product.price * ordered_product.quantity
            setattr(ordered_product, 'total_price', total_price)
            setattr(ordered_product, 'design_id', ordered_product.product.iddesign)
        self.context["order"] = order
        self.context["customer"] = order.customerid
        self.context["ordered_products"] = ordered_products
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