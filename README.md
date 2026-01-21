# Kafka-Lite Using Redis

A tiny Kafka-like playground built on **Redis Streams**.

This project provides simple helpers to:
- create/delete a topic (a Redis Stream)
- publish messages to a topic
- create/delete a consumer group
- consume messages as a consumer group member

## Prerequisites

- Python 3.10+ (tested with Python 3.12)
- A running Redis server reachable at `localhost:6379`

## Setup (Windows / PowerShell)

Create a virtual environment (optional but recommended):

```powershell
cd "C:\Users\bhara\Downloads\Kafka-Like Lite\Kafka-Like Lite"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Python dependency:

```powershell
pip install redis
```

Verify Redis is reachable:

```powershell
python -c "import redis; r=redis.StrictRedis(host='localhost',port=6379); print(r.ping())"
```

## Running Redis (pick one)

### Option A: Docker (recommended)

```powershell
docker run --name redis -p 6379:6379 -d redis:7
```

### Option B: Memurai (Windows-native)

Install Memurai, start the Memurai service, then confirm it listens on port 6379.

### Option C: WSL

Install Redis inside WSL and run it there. Ensure port 6379 is accessible from Windows.

## Quick Demo

Run an end-to-end demo (create topic → create group → publish → consume):

```powershell
python -c "from topic_manager import create_topic; from consumer_group_manager import create_consumer_group; from producer import publish_message; from consumer import consume_messages; topic='demo-topic'; group='demo-group'; consumer='c1'; create_topic(topic); create_consumer_group(topic, group); publish_message(topic, 'hello from redis streams'); consume_messages(topic, group, consumer, count=10)"
```

## Files

- `topic_manager.py` — create/delete topics (Redis streams)
- `producer.py` — publish messages (XADD)
- `consumer_group_manager.py` — manage consumer groups (XGROUP)
- `consumer.py` — consume and ACK messages (XREADGROUP / XACK)

## Notes / Known Limitations

- `create_topic()` currently uses `maxlen=retention_ms` on `XADD`, which **does not implement time-based retention** (it caps stream length, and the units are entries, not milliseconds).
- The helpers assume Redis is at `localhost:6379`. Update the `redis.StrictRedis(...)` lines in each file if you need a different host/port.
