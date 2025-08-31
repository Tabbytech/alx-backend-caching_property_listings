from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties, get_redis_cache_metrics
from .models import Property


# View with low-level caching (queryset)
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({"data": properties}, safe=False)


# View with response caching (15 minutes)
@cache_page(60 * 15)
def property_list_cached(request):
    properties = Property.objects.all().values(
        "id", "title", "description", "price", "location", "created_at"
    )
    return JsonResponse({"data": list(properties)}, safe=False)


# Redis metrics view
def cache_metrics(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse({"data": metrics})
