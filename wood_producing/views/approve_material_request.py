from .views import *


class ApproveMaterialRequest(RoleRequiredView):
    user_role = 2
    form = None
    template_path = "wood_producing/producing_manager/approve_material_request.html"

    def update_get_context(self, request, *args, **kwargs):
        material_request = Materialrequest.objects.get(id=kwargs.get('material_request_id'))
        setattr(material_request, 'create_at', material_request.create_at.strftime('%m/%d/%Y'))

        material = material_request.material
        material_of_providers = Materialofprovider.objects.filter(materialid=material)

        # get materialOfProviderInStorage
        material_by_storages = {}
        for material_of_provider in material_of_providers:
            mopises = Materialofproviderinstorage.objects.filter(materialofproviderid=material_of_provider)
            for mopis in mopises:
                if material_by_storages.get(str(mopis.storageid.id)) is None:
                    material_by_storages[str(mopis.storageid.id)] = [mopis]
                else:
                    material_by_storages[str(mopis.storageid.id)].append(mopis)
        
        print(material_by_storages)
        storage_info = []
        for key in material_by_storages:
            material_by_storage = material_by_storages.get(key)
            quantity = 0
            for mopis in material_by_storage:
                quantity += mopis.quantity
            
            storage = Storage.objects.get(id=int(key))
            setattr(storage, 'total_quantity', quantity)
            storage_info.append(storage)
        self.context["storages"] = storage_info
        self.context["material_request"] = material_request
        return 

    def post(self, request, *args, **kwargs):
        post_dict = request.POST
        material_id = request.POST.get("material_id")
        material_request_id = request.POST.get("material_request_id")
        print("request.POST: {}".format(request.POST))

        storage_material_info = []
        for key in post_dict:
            value = post_dict.get(key)
            if value == "":
                value = "0"
            strs = key.split(",")
            print("strs: {}".format(strs))
            if len(strs) == 2 and "storage" in strs[0] and strs[1] == "quantity":
                print("reached here")
                storage_strs = strs[0].split("-")
                if len(storage_strs) == 2:
                    print("reached abcd here    ")
                    storage_material_info.append({
                        "id": int(storage_strs[1]),
                        "quantity": value
                    })
        

        print(storage_material_info)
        material = Material.objects.get(id=material_id)
        material_request = Materialrequest.objects.get(id=material_request_id)
        for storage_material in storage_material_info:
            storage = Storage.objects.get(id=storage_material.get("id"))
            mopises = Materialofproviderinstorage.objects.filter(storageid=storage, materialofproviderid__materialid=material).order_by("quantity")

            need_material = int(storage_material.get("quantity"))
            for mopis in mopises:
                if need_material <= 0:
                    break
                new_quantity = max(mopis.quantity - need_material, 0)
                need_material -= mopis.quantity - new_quantity
                mopis.quantity = new_quantity
                mopis.save()
        
        material_request.is_approved = True
        material_request.save()
        return HttpResponseRedirect("/storage_manager/list_material_request")
            

    
class ListMaterialRequest(RoleRequiredView):
    user_role = 2
    form = None
    template_path = "wood_producing/producing_manager/list_material_request.html"

    def update_get_context(self, request, *args, **kwargs):
        material_requests = Materialrequest.objects.filter(is_approved=False)
        for material_request in material_requests:
            setattr(material_request, 'create_at', material_request.create_at.strftime('%m/%d/%Y'))

        self.context["material_requests"] = material_requests