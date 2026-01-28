import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def consume_messages(topic_name, consumer_group, consumer_name, count=1):
    try:
        # Consume messages as part of a consumer group
        messages = redis_client.xreadgroup(groupname=consumer_group, consumername=consumer_name,
                                           streams={topic_name: '>'}, count=count)
        if messages:
            for stream, stream_messages in messages:
                for message_id, fields in stream_messages:
                    print(f"Consumed message: {fields}")
                    redis_client.xack(topic_name, consumer_group, message_id)  # Acknowledge the message
    except Exception as e:
        print(f"Error consuming messages: {str(e)}")