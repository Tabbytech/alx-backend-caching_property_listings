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

        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0

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
