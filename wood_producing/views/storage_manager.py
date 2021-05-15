from .views import *

class ImportMaterialFromProvider(RoleRequiredView):
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)

    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)

class MaterialBaseForm(forms.Form):
    search_keyword = forms.CharField()


class MaterialBase(RoleRequiredView):
    user_role = 2 
    form = MaterialBaseForm
    template_path = "wood_producing/producing_manager/material_base.html"
    direct_url={}
    
    def update_get_context(self, request, *args, **kwargs):
        page_size = settings.PAGE_SIZE
        kw = request.GET.get('material_name')
        materials = Material.objects.all()
        if kw is not None :
            materials = materials.filter(name__contains=kw)
        self.context['materials']=materials
        return None

    def update_post_context(self, request, *args, **kwargs):
        print("post request")
        id = request.POST.get('id')
        print(id)
        material = Material.objects.get(pk=id)
        material.delete()
        return None

class AddMaterialForm(forms.Form):
    material_name = forms.CharField()
    type = forms.CharField()

class AddMaterial(RoleRequiredView):
    user_role = 2
    form = AddMaterialForm
    template_path = "wood_producing/producing_manager/material_add.html"
    direct_url = {
    }
    
    """ Get Management view
        Delete, Add, Update be implemented in api.py
    """
    def update_get_context(self, request, *args, **kwargs):

        return None
    
    def update_post_context(self, request, *args, **kwargs):
        material = Material.objects.create(
            name = self.cleaned_data.get('material_name'),
            type = self.cleaned_data.get('type'),
            desc = "test",
            discriminator = 1
        )
        material.save()
        return None

class EditMaterialForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    desc = forms.CharField()

class EditMaterial(RoleRequiredView):
    user_role = 2
    form = EditMaterialForm
    template_path = "wood_producing/producing_manager/material_edit.html"
    direct_url={}
    
    def update_get_context(self, request, *args, **kwargs):
        id = kwargs['material_id']
        material = Material.objects.get(pk=id)
        self.context['material']=material
        return None

    def update_post_context(self, request, *args, **kwargs):
        id = kwargs['material_id']
        material = Material.objects.get(pk=id)
        material.name = self.cleaned_data.get('name')
        material.type = self.cleaned_data.get('type')
        material.desc = self.cleaned_data.get('desc')
        material.save()
        return None

class DeleteMaterial(RoleRequiredView):
    user_role = 2

class ProductManagement(RoleRequiredView):
    """ Get Management view
        Delete, Add, Update be implemented in api.py
    """
    def update_get_context(self, request, *args, **kwargs):
        return None
    
    def update_post_context(self, request, *args, **kwargs):
        return None