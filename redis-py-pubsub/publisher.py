import redis
import time
import json


redis_host = 'localhost'
redis_port = '6379'
channel = "hello-channel"

publisher = redis.Redis(host=redis_host, port=redis_port)
count = 0
while True:
    count += 1
    message = {
        'text': 'Hello World',
        'count': count
    }
    publisher.publish(channel, json.dumps(message))
    print('Message published:', json.dumps(message, indent=4))
    time.sleep(1)