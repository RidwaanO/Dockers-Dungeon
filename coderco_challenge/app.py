# app.py
import os
from flask import Flask
from redis import Redis

redis_host = os.getenv('REDIS_HOST','redis')
redis_port = int(os.getenv('REDIS_PORT','6379'))

redis = Redis(host=redis_host, port=redis_port)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, and welcome to my application'
    
@app.route('/count')
def index():
    redis.incr('hits')
    count = redis.get('hits').decode('utf-8')  # Decode the byte result
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)