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