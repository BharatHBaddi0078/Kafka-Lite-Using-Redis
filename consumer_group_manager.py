import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def create_consumer_group(topic_name, group_name):
    try:
        redis_client.xgroup_create(topic_name, group_name)
        print(f"Created consumer group '{group_name}' for topic '{topic_name}'")
    except Exception as e:
        print(f"Error creating consumer group: {str(e)}")

def delete_consumer_group(topic_name, group_name):
    try:
        redis_client.xgroup_destroy(topic_name, group_name)
        print(f"Deleted consumer group '{group_name}'")
    except Exception as e:
        print(f"Error deleting consumer group: {str(e)}")