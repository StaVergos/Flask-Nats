from flask import Flask
import asyncio

from services.nats_service import nats_handler
from services.nats_test import main

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi, from first api'


@app.route('/async')
def async_call():
    asyncio.run(main())

    return 'Run async'
