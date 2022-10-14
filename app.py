from flask import Flask, request
import asyncio

from services.nats_test import main

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello there!'


@app.route('/async')
def async_call():
    json_data = request.get_json()
    people_id = json_data['people_id']
    asyncio.run(main(people_id))

    return 'Run async'
