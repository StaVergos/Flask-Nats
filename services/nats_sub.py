import asyncio
import os
import signal
import nats


async def main():
    nc = await nats.connect("0.0.0.0:4222")

    async def closed_cb():
        print("Connection to NATS is closed.")
        await asyncio.sleep(0.1)
        asyncio.get_running_loop().stop()

    print(f"Connected to NATS at {nc.connected_url.netloc}...")

    async def subscribe_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))
        # await msg.respond(b'I can help!')

    # Basic subscription to receive all published messages
    # which are being sent to a single topic 'discover'
    await nc.subscribe("help", cb=subscribe_handler)

    def signal_handler():
        if nc.is_closed:
            return
        print("Disconnecting...")
        asyncio.create_task(nc.close())

    # Keep it running forever
    await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass
