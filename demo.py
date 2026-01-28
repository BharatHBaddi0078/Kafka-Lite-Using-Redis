import time

from consumer import consume_messages
from consumer_group_manager import create_consumer_group
from producer import publish_message
from topic_manager import create_topic


def main() -> None:
    topic = f"demo-topic-{int(time.time())}"
    group = "demo-group"
    consumer_name = "c1"

    create_topic(topic)
    create_consumer_group(topic, group)
    publish_message(topic, "hello from redis streams")
    consume_messages(topic, group, consumer_name, count=10)


if __name__ == "__main__":
    main()
