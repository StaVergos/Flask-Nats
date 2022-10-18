from flask import Flask, request
import asyncio

from services.nats_pub import publish_nats
from services.nats_req_rep import sub

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


@app.route('/req_rep')
def req_rep():
    sub()
    return 'Runned req_rep'
