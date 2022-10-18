import asyncio

import nats
from nats.errors import TimeoutError, NoRespondersError


async def main():
    nc = await nats.connect("0.0.0.0:4222")

    async def greet_handler(msg):
      name = msg.subject[6:]
      reply = f'Hello, {name}'
      await msg.respond(reply.encode("utf8"))

    sub = await nc.subscribe("greet.*", cb=greet_handler)

    rep = await nc.request("greet.joe", b'', timeout=0.5)
    print(f"{rep.data}")

    rep = await nc.request("greet.sue", b'', timeout=0.5)
    print(f"{rep.data}")

    await sub.drain()

    try:
        await nc.request("greet.joe", b'', timeout=0.5)
    except NoRespondersError:
        print("no responders")

    await nc.drain()


if __name__ == '__main__':
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())
