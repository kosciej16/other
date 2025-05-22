import asyncio
import aio_pika


async def main():
    url = ""
    connection = await aio_pika.connect_robust(url)
    queue_name = "acquisitor-parse-result"
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)


res = asyncio.run(main())
