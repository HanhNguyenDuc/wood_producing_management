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

