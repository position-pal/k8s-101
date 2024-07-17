from flask import Flask, request
import redis
import os

import time

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

max_retries = 5
for attempt in range(max_retries):
    try:
        r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        r.ping()
        print("Connected to Redis")
        break
    except redis.ConnectionError as e:
        print(f"Redis connection error: {e}")
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)
        else:
            r = None
@app.route('/')
def index():
    return "Hello Valerio and Luca!"

@app.route('/set', methods=['POST'])
def set_value():
    key = request.form['key']
    value = request.form['value']
    r.set(key, value)
    return f"Key {key} set to {value}"

@app.route('/get', methods=['GET'])
def get_value():
    key = request.args.get('key')
    value = r.get(key)
    return f"Value for key {key} is {value}"

@app.route('/error', methods=['GET'])
def error():
    raise Exception("This is a test exception")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)