from django.http import JsonResponse
from .utils import get_all_properties, get_redis_cache_metrics

def property_list(request):
    properties = get_all_properties()
    return JsonResponse(properties, safe=False)

def cache_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)
