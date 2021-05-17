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
    return JsonResponse({
        "msg":"sucess"
    })

@csrf_exempt
def import_material(request):
    provider_id = request.session['provider_id']
    print(provider_id)
    material_id = request.POST.get('id')
    quantity = request.POST.get('quantity')
    price = request.POST.get('price')
    print(material_id)
    print(quantity)
    print(price)
# ben tren chay ok
    material_of_provider = Materialofprovider.objects.get_or_create(
        providerid=provider_id,
        materialid=material_id,
        defaults={'price':0}
    )
    print("check1")
    material_of_provider.price = price
    print("check2")
    material_of_provider.save()
    return JsonResponse({
        "msg":"Sucess"
    })