import redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def publish_message(topic_name, message):
    try:
        # Use Redis Streams to add message to the topic
        message_id = redis_client.xadd(topic_name, fields={'message': message})
        print(f"Message published to topic '{topic_name}' with ID: {message_id}")
        return message_id
    except Exception as e:
        print(f"Error publishing message: {str(e)}")
        return None