import requests
import nats
import json


async def main(people_id):

    url = f"https://swapi.dev/api/people/{people_id}/"

    # Connect to NATS!
    nc = await nats.connect("0.0.0.0:4222")

    # Receive messages on subject 'say hi'
    sub = await nc.subscribe("swapi")

    # Publish a message to 'foo'
    resp = requests.get(url)
    resp_processed = resp.json()
    sw_hero = {'name': resp_processed['name'], 'height': resp_processed['height']}
    await nc.publish("swapi", json.dumps(sw_hero).encode())

    # Process a message
    msg = await sub.next_msg()
    data = json.loads(msg.data.decode())
    print("Received:", data)

    # Close NATS connection
    await nc.close()
