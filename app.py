from flask import Flask, request
import asyncio

from services.nats_pub import publish_nats

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello there!'


@app.route('/sw_req')
def sw_req():
    json_data = request.get_json()
    people_id = json_data['people_id']
    asyncio.run(publish_nats(people_id))

    return 'Runned sw_req'
