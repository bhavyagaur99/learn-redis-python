import redis
import json


redis_host = 'localhost'
redis_port = '6379'
channel = "hello-channel"
rd = redis.Redis(host=redis_host, port=redis_port)
subscriber = rd.pubsub()
subscriber.subscribe(channel)

for buffer in subscriber.listen():
    if buffer['type'] != 'message':
        print('buffer type:', buffer['type'], ', skipping')
        continue
    msg = json.loads(buffer['data'].decode('utf8'))
    print('message:', json.dumps(msg, indent=4))