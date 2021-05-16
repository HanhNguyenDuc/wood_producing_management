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
        page_num = request.GET.get("page_num")
        kw = request.GET.get('material_name')
        materials = Material.objects.all()
        if kw is not None :
            materials = materials.filter(name__contains=kw)
        p = Paginator(materials,page_size)
        cur_page = p.page(1)
        if page_num is not None :
            cur_page = p.page(page_num)
        self.context['num_page'] = p.num_pages
        self.context['page'] = range(1,p.num_pages+1)
        self.context['materials'] = cur_page.object_list
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
    desc = forms.CharField()

class AddMaterial(RoleRequiredView):
    user_role = 2
    form = AddMaterialForm
    template_path = "wood_producing/producing_manager/material_add.html"
    
    """ Get Management view
        Delete, Add, Update be implemented in api.py
    """
    def update_get_context(self, request, *args, **kwargs):

        return None
    
    def update_post_context(self, request, *args, **kwargs):
        material = Material.objects.create(
            name = self.cleaned_data.get('material_name'),
            type = self.cleaned_data.get('type'),
            desc = self.cleaned_data.get('desc'),
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

class ProductManagement(RoleRequiredView):
    user_role = 2 
    form = None
    template_path = "wood_producing/product_manager/product_base.html"
    """ Get Management view
        Delete, Add, Update be implemented in api.py
    """
    def update_get_context(self, request, *args, **kwargs):
        page_size = settings.PAGE_SIZE
        kw = request.GET.get('product_name')
        products = Product.objects.all()
        if kw is not None :
            products = products.filter(name__contains=kw)
        self.context['products']=products
        return None
    
    def update_post_context(self, request, *args, **kwargs):
        return None

class AddProductForm(forms.Form):
    name = forms.CharField()
    id = forms.CharField()
    type = forms.CharField()
    price = forms.CharField()
    desc = forms.CharField()

class AddProduct(RoleRequiredView):
    user_role = 2
    form = AddProductForm
    template_path = "wood_producing/product_manager/product_add.html"

    def update_get_context(self, request, *args, **kwargs):
        return None

    def update_post_context(self, request, *args, **kwargs):
        product = Product.objects.create(
            name = self.cleaned_data.get('name'),
            id = self.cleaned_data.get('id'),
            type = self.cleaned_data.get('type'),
            price = self.cleaned_data.get('price'),
            desc = self.cleaned_data.get('desc')
        )
        product.save()
        return None


class EditProductForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField()
    id = forms.CharField()
    price = forms.CharField()
    desc = forms.CharField()

class EditProduct(RoleRequiredView):
    user_role = 2
    form = EditProductForm
    template_path = "wood_producing/product_manager/product_edit.html"

    def update_get_context(self, request, *args, **kwargs):
        id = kwargs['product_id']
        product = Product.objects.get(pk=id)
        self.context['product']=product
        return None

    def update_post_context(self, request, *args, **kwargs):
        id = kwargs['product_id']
        product = Product.objects.get(pk=id)
        product.name = self.cleaned_data.get('name')
        product.type = self.cleaned_data.get("type")
        product.id = self.cleaned_data.get('id')
        product.price = self.cleaned_data.get('price')
        product.desc = self.cleaned_data.get('desc')
        product.save()
        return None


class ImportChooseMaterial(RoleRequiredView):
    user_role = 2
    form = None
    template_path = "wood_producing/import_material/choose_material.html"
    def update_get_context(self, request, *args, **kwargs):
        return super().update_get_context(request, *args, **kwargs)
    def update_post_context(self, request, *args, **kwargs):
        return super().update_post_context(request, *args, **kwargs)
