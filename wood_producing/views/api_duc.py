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
    request.session['provider']=provider
    return JsonResponse({
        "msg":"sucess"
    })