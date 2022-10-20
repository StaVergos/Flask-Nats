import asyncio

import nats
from nats.errors import ConnectionClosedError, NoServersError, TimeoutError


async def main():
    nc = await nats.connect("0.0.0.0:4222")

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    try:
        response = await nc.request("help", b'help me', timeout=0.5)
        print("Received response: {message}".format(
            message=response.data.decode()))
    except TimeoutError:
        print("Request timed out")

    # Terminate connection to NATS.
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(main())
