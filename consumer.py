import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def consume_messages(topic_name, consumer_group, consumer_name, count=1):
    try:
        # Consume messages as part of a consumer group
        messages = redis_client.xreadgroup(groupname=consumer_group, consumername=consumer_name,
                                           streams={topic_name: '>'}, count=count)
        if messages:
            for message in messages:
                stream, msg = message
                print(f"Consumed message: {msg}")
                redis_client.xack(topic_name, consumer_group, msg[0])  # Acknowledge the message
    except Exception as e:
        print(f"Error consuming messages: {str(e)}")