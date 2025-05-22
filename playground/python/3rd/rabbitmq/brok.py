from faststream.rabbit import RabbitBroker


url = "amqp://localhost:5672"
broker = RabbitBroker(url=url, max_consumers=200, asyncapi_url="0.0.0.0:8000", timeout=5)
