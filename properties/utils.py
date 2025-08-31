from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    """Return all properties, caching result in Redis for 1 hour."""
    properties = cache.get("all_properties")

    if not properties:
        logger.info("Fetching properties from DB (cache miss)")
        properties = list(Property.objects.all().values(
            "id", "title", "description", "price", "location", "created_at"
        ))
        cache.set("all_properties", properties, timeout=3600)
    else:
        logger.info("Fetching properties from Redis (cache hit)")

    return properties


def get_redis_cache_metrics():
    """
    Get Redis cache hit/miss metrics using django-redis.
    Returns a dictionary with hits, misses, and hit ratio.
    """
    try:
        client = cache.client.get_client(write=False)
        info = client.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total = hits + misses
        hit_ratio = (hits / total) if total > 0 else 0

        metrics = {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 2)
        }

        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics

    except Exception as e:
        logger.error(f"Error fetching Redis cache metrics: {e}")
        return {"error": str(e)}
