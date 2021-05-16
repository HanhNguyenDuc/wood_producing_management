from .views import *


class ApproveMaterialRequest(RoleRequiredView):
    user_role = 2
    form = None
    template_path = "wood_producing/producing_manager/approve_material_request.html"

    def update_get_context(self, request, *args, **kwargs):
        material_request = Materialrequest.objects.get(id=kwargs.get('material_request_id'))
        setattr(material_request, 'create_at', material_request.create_at.strftime('%m/%d/%Y'))

        self.context["material_request"] = material_request

    
class ListMaterialRequest(RoleRequiredView):
    user_role = 2
    form = None
    template_path = "wood_producing/producing_manager/list_material_request.html"

    def update_get_context(self, request, *args, **kwargs):
        material_requests = Materialrequest.objects.filter(is_approved=False)
        for material_request in material_requests:
            setattr(material_request, 'create_at', material_request.create_at.strftime('%m/%d/%Y'))

        self.context["material_requests"] = material_requests