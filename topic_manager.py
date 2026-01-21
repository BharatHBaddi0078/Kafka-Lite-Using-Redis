import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def create_topic(topic_name, retention_ms=3600000):
    try:
        # Setting topic retention in milliseconds
        redis_client.xadd(topic_name, fields={'system': 'Initialized'}, maxlen=retention_ms)
        print(f"Created topic '{topic_name}' with retention {retention_ms}ms")
    except Exception as e:
        print(f"Error creating topic: {str(e)}")

def delete_topic(topic_name):
    try:
        redis_client.delete(topic_name)
        print(f"Deleted topic '{topic_name}'")
    except Exception as e:
        print(f"Error deleting topic: {str(e)}")