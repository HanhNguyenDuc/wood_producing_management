from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

@csrf_exempt
def add_user(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    customer = Customer(name=name, phone=phone, address=address)
    customer.save()

    return JsonResponse({
        "msg": "Success",
        "material_request": {
          "id": customer.id,
        }
    })

@csrf_exempt
def search_product_by_name(request):
    name = request.GET.get('search_data')
    products = Product.objects.filter(name__contains=name)
    res_arr = [] 
    for product in products:
      res_arr.append({"name": product.name, "id": product.id, "price": product.price, "iddesign": product.iddesign})
    return JsonResponse({
        "msg": "Success",
        "material_request": {
          "products": res_arr,
        }
    })

@csrf_exempt
def search_customer_by_name(request):
    name = request.GET.get('search_data')
    customers = Customer.objects.filter(name__contains=name)
    res_arr = [] 
    for customer in customers:
      res_arr.append({"name": customer.name, "id": customer.id, "phone": customer.phone, "address": customer.address})
    return JsonResponse({
        "msg": "Success",
        "material_request": {
          "customers": res_arr,
        }
    })