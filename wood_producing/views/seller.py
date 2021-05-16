from .views import *
# vao phan tao don hang
class CreateOrder(RoleRequiredView):
    user_role = 4
    template_path = "wood_producing/create_order/base.html"
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)
# ra file PDF
class PublishOrder(RoleRequiredView): 
    user_role = 4
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)
    
    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)