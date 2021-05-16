from .views import *
from django.views.decorators.csrf import csrf_exempt

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