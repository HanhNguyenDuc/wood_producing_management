from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from jsonmerge import merge

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@csrf_exempt
def delete_task(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    task_id = int(request.POST.get("task_id"))
    task = Task.objects.get(id=task_id)
    task.delete()
    return JsonResponse({
        "msg": "Success",
    })

@csrf_exempt
def statistic_profit(request):
    start_date = int(request.POST.get("date-input-1").split("-")[0])
    end_date = int(request.POST.get("date-input-2").split("-")[0])
    response = {
        "labels": [],
        "income": {},
        "product_labels": [],
        "product_income": {}
    }
    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT TotalIncome FROM wood_producing_exportbill WHERE NOT (Date > \'2021-%s-30\' OR Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
        response["income"][temp_date] = int(result["TotalIncome"])
        response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT Name FROM wood_producing_product"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = dictfetchall(cursor)
            for product_name in result["Name"]:
                response["product_labels"].append(product_name)
                response["product_income"][product_name] = 0

        sql = "SELECT wood_producing_product.Name, wood_producing_orderedproduct.Price, wood_producing_orderedproduct.Quantity FROM wood_producing_orderedproduct, wood_producing_product, wood_producing_order WHERE wood_producing_orderedproduct.Product = wood_producing_product.ID AND wood_producing_order.ID = wood_producing_orderedproduct.order_id AND NOT (wood_producing_order.duedate > \'2021-%s-30\' OR wood_producing_order.duedate < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            for product_name in result["Name"]:
                response["product_income"][product_name] += int(result["Quantity"])*int(result["Price"])
        temp_date += 1
    return merge({"msg": "Success"},response)

@csrf_exempt
def statistic_production(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    start_date = int(request.POST.get("date-input-1").split("-")[0])
    end_date = int(request.POST.get("date-input-2").split("-")[0])
    response = {
        "labels": [],
        "quantity": {},
        "product_labels": [],
        "product_quantity": {},
        "workshop_labels": [],
        "workshop_quantity": {},
    }
    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT wood_producing_productexported.Quantity FROM wood_producing_exportbill, wood_producing_productexported WHERE wood_producing_productexported.ExportBillID = wood_producing_exportbill.ID AND NOT (wood_producing_exportbill.Date > \'2021-%s-30\' OR wood_producing_exportbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
        count = 0
        for i in result["quantity"]:
            count += int(i)
        response["Quantity"][temp_date] = count
        response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT Name FROM wood_producing_product"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = dictfetchall(cursor)
            for product_name in result["Name"]:
                response["product_labels"].append(product_name)
                response["product_quantity"][product_name] = 0

        sql = "SELECT wood_producing_product.Name, wood_producing_product.Quantity FROM wood_producing_exportbill, wood_producing_product, wood_producing_productexported WHERE wood_producing_productexported.Product = wood_producing_product.ID AND wood_producing_productexported.ExportBillID = wood_producing_exportbill.ID AND NOT (wood_producing_exportbill.Date > \'2021-%s-30\' OR wood_producing_exportbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            for product_name in result["Name"]:
                response["product_quantity"][product_name] += int(result["Quantity"])
        temp_date += 1

    while temp_date < end_date:
        sql = "SELECT UserID FROM wood_producing_task"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = dictfetchall(cursor)
            for workshop in result["UserID"]:
                response["workshop_labels"].append("Xưởng " + workshop)
                response["workshop_quantity"][workshop] = 0

        sql = "SELECT UserID, quantity FROM wood_producing_task WHERE NOT (estimated > \'2021-%s-30\' OR estimated < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            for workshop in result["UserID"]:
                response["workshop_quantity"][workshop] += int(result["quantity"])
        temp_date += 1
    return merge({"msg": "Success"},response)

@csrf_exempt
def statistic_material(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    start_date = int(request.POST.get("date-input-1").split("-")[0])
    end_date = int(request.POST.get("date-input-2").split("-")[0])
    response = {
        "labels": [],
        "material_quantity_total": {},
        "material_labels": [],
        "material_quantity": {},
        "provider": [],
        "provider_material_quantity":{}
    }

    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT wood_producing_importbill.ID FROM wood_producing_importedmaterial, wood_producing_importbill WHERE wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
        response["material_quantity_total"][temp_date] = len(result["ID"])
        response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT Name FROM wood_producing_material"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = dictfetchall(cursor)
            for material_name in result["Name"]:
                response["material_labels"].append(material_name)
                response["material_quantity"][material_name] = 0

        sql = "SELECT wood_producing_material.Name, wood_producing_material.Quantity FROM wood_producing_material, wood_producing_importedmaterial, wood_producing_importbill WHERE wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND wood_producing_importedmaterial.Material = wood_producing_material.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            for material_name in result["Name"]:
                response["material_quantity"][material_name] += int(result["Quantity"])
        temp_date += 1

    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT Name FROM wood_producing_provider"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = dictfetchall(cursor)
            for name in result["Name"]:
                response["provider"].append(name)
                response["provider_material_quantity"][name] = 0

        sql = "SELECT wood_producing_provider.Name, wood_producing_material.Quantity FROM wood_producing_material, wood_producing_provider, wood_producing_importedmaterial, wood_producing_importbill WHERE wood_producing_importbill.ProviderID = wood_producing_provider.ID AND wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND wood_producing_importedmaterial.Material = wood_producing_material.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            for provider in result["Name"]:
                response["provider_material_quantity"][provider] += int(result["Quantity"])
        temp_date += 1
    
    return merge({"msg": "Success"},response)

def create_material_request(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    material_id = request.POST.get('material_id')
    task_id = request.POST.get('task_id')
    quantity = request.POST.get('quantity')

    material = Material.objects.get(id=material_id)
    task = Task.objects.get(id=task_id)
    mr = Materialrequest(material=material, taskid=task, quantity=quantity)
    mr.save()

    return JsonResponse({
        "msg": "Success",
        "material_request": {
            "id": mr.id,
        }
    })

@csrf_exempt
def delete_material(request):
    id = int(request.POST.get("material_id"))
    material = Material.objects.get(pk=id)
    material.delete()
    return JsonResponse({
        "msg": "Success",
    })
        
@csrf_exempt
def delete_product(request):
    id = int(request.POST.get('product_id'))
    product = Product.objects.get(pk=id)
    product.delete()
    return JsonResponse({
        "msg":"Sucess",
    })

