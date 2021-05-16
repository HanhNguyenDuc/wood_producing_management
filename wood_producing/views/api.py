from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from jsonmerge import merge
import logging

logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s', level=logging.INFO)

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
    start_date = int(request.POST.get("start_date").split("-")[1])
    end_date = int(request.POST.get("end_date").split("-")[1])
    response = {
        "labels": [],
        "income": [],
        "product_labels": [],
        "product_income_detail": []
    }
    temp_date = start_date
    while temp_date <= end_date:
        sql = "SELECT TotalIncome FROM wood_producing_exportbill WHERE NOT (Date > \'2021-%s-30\' OR Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            logging.info("result: ")
            logging.info(result)
        if len(result) > 0:
            response["income"].append(int(result[0]["TotalIncome"]))
            response["labels"].append("Tháng "+str(temp_date))
        else:
            response["income"].append(0)
            response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    temp_date = start_date
    sql = "SELECT Name FROM wood_producing_product"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        if len(result) > 0 :
            for product_name in result:
                response["product_labels"].append(product_name["Name"])
                response["product_income_detail"].append({
                    'label': product_name["Name"],
                    'income': [],
                    'temp': 0
                })

    while temp_date <= end_date:
        sql = "SELECT wood_producing_product.Name, wood_producing_orderedproduct.Price, wood_producing_orderedproduct.Quantity FROM wood_producing_orderedproduct, wood_producing_product, wood_producing_order WHERE wood_producing_orderedproduct.Product = wood_producing_product.ID AND wood_producing_order.ID = wood_producing_orderedproduct.order_id AND NOT (wood_producing_order.duedate > \'2021-%s-30\' OR wood_producing_order.duedate < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            logging.info("result: ")
            logging.info(result)
            if len(result) > 0:
                for product_name in result:
                    for product in response["product_income_detail"]:
                        if product["label"] == product_name["Name"]:
                            product["temp"] += int(product_name["Quantity"])*int(product_name["Price"])

        for product in response["product_income_detail"]:
            product["income"].append(product["temp"])
            product["temp"] = 0
        temp_date += 1
    logging.info(response)
    return JsonResponse(merge({"msg": "Success"},response))

@csrf_exempt
def statistic_production(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    start_date = int(request.POST.get("start_date").split("-")[1])
    end_date = int(request.POST.get("end_date").split("-")[1])
    response = {
        "labels": [],
        "quantity": [],
        "product_labels": [],
        "product_quantity_detail": [],
        "workshop_labels": [],
        "workshop_quantity_detail": [],
    }
    temp_date = start_date
    while temp_date < end_date:
        sql = "SELECT wood_producing_orderedproduct.Quantity FROM wood_producing_order, wood_producing_orderedproduct WHERE wood_producing_orderedproduct.order_id = wood_producing_order.ID AND NOT (wood_producing_order.duedate > \'2021-%s-30\' OR wood_producing_order.duedate < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
        count = 0
        if len(result) > 0:
            for i in result:
                count += int(i["Quantity"])
        response["quantity"].append(count)
        response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    sql = "SELECT Name FROM wood_producing_product"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        for product_name in result:
            response["product_labels"].append(product_name["Name"])
            response["product_quantity_detail"].append({
                'label': product_name["Name"],
                'quantity': [],
                'temp':0
            })

    temp_date = start_date        
    while temp_date < end_date:
        sql = "SELECT wood_producing_product.Name, wood_producing_orderedproduct.Quantity FROM wood_producing_order, wood_producing_orderedproduct, wood_producing_product WHERE wood_producing_orderedproduct.Product = wood_producing_product.ID AND wood_producing_orderedproduct.order_id = wood_producing_order.ID AND NOT (wood_producing_order.duedate > \'2021-%s-30\' OR wood_producing_order.duedate < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            if len(result) > 0:
                for product_name in result:
                    for product in response["product_quantity_detail"]:
                        if product["label"] == product_name["Name"]:
                            product["temp"] += int(product_name["Quantity"])

        for product in response["product_quantity_detail"]:
            product["quantity"].append(product["temp"])
            product["temp"] = 0
        temp_date += 1

    sql = "SELECT DISTINCT UserID FROM wood_producing_task"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        if len(result) > 0:
            for workshop in result:
                response["workshop_labels"].append(str(workshop["UserID"]))
                response["workshop_quantity_detail"].append({
                    'label': str(workshop["UserID"]),
                    'quantity': [],
                    'temp':0
                })
    temp_date = start_date  
    while temp_date < end_date:
        sql = "SELECT UserID, quantity FROM wood_producing_task WHERE NOT (estimated > \'2021-%s-30\' OR estimated < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            logging.info(result)
            if len(result) > 0:
                for temp_result in result:
                    for workshop in response["workshop_quantity_detail"]:
                        if workshop["label"] == str(temp_result["UserID"]):
                            workshop["temp"] += int(temp_result["quantity"])
        for workshop in response["workshop_quantity_detail"]:
            workshop["quantity"].append(workshop["temp"])
            workshop["temp"] = 0        
        temp_date += 1

    logging.info(response)
    return JsonResponse(merge({"msg": "Success"},response))

@csrf_exempt
def statistic_material(request):
    if request.method != 'POST':
        return JsonResponse({
            "msg": "Method is not allowed",
        })
    start_date = int(request.POST.get("start_date").split("-")[1])
    end_date = int(request.POST.get("end_date").split("-")[1])
    response = {
        "labels": [],
        "material_quantity_total": [],
        "material_labels": [],
        "material_quantity_detail": [],
        "provider_labels": [],
        "provider_quantity_detail":[]
    }

    temp_date = start_date
    while temp_date <= end_date:
        sql = "SELECT wood_producing_importedmaterial.quantity FROM wood_producing_importedmaterial, wood_producing_importbill WHERE wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
        if len(result) > 0:
            temp = 0
            for temp_result in result:
                temp += temp_result["quantity"]
            response["material_quantity_total"].append(temp)
            response["labels"].append("Tháng "+str(temp_date))
        temp_date += 1

    sql = "SELECT Name FROM wood_producing_material"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        if len(result) > 0:
            for material_name in result:
                response["material_labels"].append(material_name["Name"])
                response["material_quantity_detail"].append({
                    'label': material_name["Name"],
                    'quantity': [],
                    'temp': 0
                })

    temp_date = start_date
    while temp_date <= end_date:
        sql = "SELECT wood_producing_material.Name, wood_producing_importedmaterial.quantity FROM wood_producing_material, wood_producing_importedmaterial, wood_producing_importbill, wood_producing_materialofprovider \
            WHERE wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND wood_producing_importedmaterial.Materialofprovider = wood_producing_materialofprovider.ID \
            AND wood_producing_materialofprovider.MaterialID = wood_producing_material.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            if len(result) > 0:
                for temp_result in result:
                    for material in response["material_quantity_detail"]:
                        if material["label"] == str(temp_result["Name"]):
                            material["temp"] += int(temp_result["quantity"])
        for material in response["material_quantity_detail"]:
            material["quantity"].append(material["temp"])
            material["temp"] = 0     
        temp_date += 1

    sql = "SELECT Name FROM wood_producing_provider"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
        for temp_result in result:
            response["provider_labels"].append(temp_result["Name"])
            response["provider_quantity_detail"].append({
                'label' : temp_result["Name"],
                'quantity': [],
                'temp':0
            })

    temp_date = start_date
    while temp_date <= end_date:
        sql = "SELECT wood_producing_provider.Name, wood_producing_importedmaterial.quantity FROM wood_producing_provider, wood_producing_importedmaterial, wood_producing_importbill, wood_producing_materialofprovider \
            WHERE wood_producing_importedmaterial.ImportBillID = wood_producing_importbill.ID AND wood_producing_importedmaterial.Materialofprovider = wood_producing_materialofprovider.ID \
            AND wood_producing_materialofprovider.ProviderID = wood_producing_provider.ID AND NOT (wood_producing_importbill.Date > \'2021-%s-30\' OR wood_producing_importbill.Date < \'2021-%s-01\')"
        with connection.cursor() as cursor:
            cursor.execute(sql,[temp_date, temp_date])
            result = dictfetchall(cursor)
            if len(result) > 0:
                for temp_result in result:
                    for provider in response["provider_quantity_detail"]:
                        if provider["label"] == str(temp_result["Name"]):
                            provider["temp"] += int(temp_result["quantity"])
        for provider in response["provider_quantity_detail"]:
            provider["quantity"].append(provider["temp"])
            provider["temp"] = 0     
        temp_date += 1

    logging.info(response)
    return JsonResponse(merge({"msg": "Success"},response))

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

