from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

@csrf_exempt
def add_provider(request):
    provider = Provider.objects.create(
        name = request.POST.get('name'),
        phone = request.POST.get('phone'),
        address = request.POST.get('address'),
        desc = request.POST.get('desc')
    )
    provider.save()
    return JsonResponse({
        "msg":"sucess"
    })

@csrf_exempt
def choose_provider(request):
    provider_id = request.POST.get('provider_id')
    provider = Provider.objects.get(pk=provider_id)
    request.session['provider_id']=provider.id
    request.session['provider_id'] = provider_id
    bill = Importbill(providerid=Provider.objects.get(id=provider_id))
    bill.save()
    request.session['bill_id']=bill.id
    return JsonResponse({
        "msg":"sucess"
    })

@csrf_exempt
def import_material(request, id, quantity, price):
    provider_id = request.session['provider_id']
    print("Provier id: {}".format(provider_id))
    provider = Provider.objects.get(id=provider_id)
    material_id = id
    print("Material id: {}".format(request.session.get("bill")))
    material = Material.objects.get(id=material_id)
# ben tren chay ok
    material_of_provider = Materialofprovider.objects.get_or_create(
        providerid= provider,
        materialid= material,
        defaults={'price':0}
    )
    print(material_of_provider[0])
    material_of_provider[0].price = price
    material_of_provider[0].save()
    # bill = Importbill(providerid=Provider.objects.get(id=provider_id))
    # bill.save()
    bill = Importbill.objects.get(id=request.session['bill_id'])
    imported_material = Importedmaterial.objects.create(
        materialofprovider=material_of_provider[0],
        quantity=quantity,
        price=price,
        importbillid=bill
    )
    imported_material.save()
    return JsonResponse({
        "msg":"Sucess",
        "name": material.name,
        "type": material.type
    })