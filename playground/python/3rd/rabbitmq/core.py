from time import sleep
import pika
import logging


SERVICE_NAME = "acquisitor"

logger = logging.getLogger(__name__)


class RabbitMQPublisher:
    def __init__(self, host="localhost", port=5672, virtual_host="/", credentials=None):
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.credentials = credentials
        self.connection = None
        self.channel = None
        self.url_params = None

    def from_url(self, connection_url: str):
        self.url_params = pika.URLParameters(connection_url)

    def connect(self) -> None:
        """Establish connection with RabbitMQ"""
        try:
            parameters = pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                virtual_host=self.virtual_host,
                credentials=self.credentials,
                heartbeat=3,  # Heartbeat timeout (in seconds)
            )
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            print("Connected to RabbitMQ")
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            raise

    def publish_message(self, exchange: str, routing_key: str, message: str) -> bool:
        """Publish message with reconnection logic"""
        try:
            if not self.connection or self.connection.is_closed:
                self.connect()

            self.channel.basic_publish(
                exchange=exchange,
                routing_key=routing_key,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2  # Make message persistent
                ),
            )
            return True
        except pika.exceptions.AMQPConnectionError:
            print("Connection lost. Attempting to reconnect...")
            self.connect()
            return self.publish_message(exchange, routing_key, message)
        except Exception as e:
            print(f"Failed to publish message: {str(e)}")
            return False

    def close(self):
        """Close the connection"""
        if self.connection and not self.connection.is_closed:
            self.connection.close()

    def delete(self, queue):
        connection = pika.BlockingConnection(self.url_params)

        channel = connection.channel()
        channel.queue_delete(queue=queue)

    def declare_queue(self, queue_name: str, durable=True, auto_delete=False):
        """Declare a queue if it doesn't exist"""
        try:
            self.channel.queue_declare(
                queue=queue_name,
                durable=durable,  # Queue survives broker restart
                auto_delete=auto_delete,  # Don't delete queue when consumer disconnects
            )
            logger.info(f"Queue {queue_name} declared")
        except Exception as e:
            logger.error(f"Failed to declare queue: {str(e)}")
            raise


credentials = pika.PlainCredentials(username="guest", password="guest")

if __name__ == "__main__":
    publisher = RabbitMQPublisher(credentials=credentials)
    publisher.connect()

    queue_name = "test_queue"
    publisher.declare_queue(queue_name)
    publisher.publish_message("", queue_name, "Hello World!")
    sleep(7)
    publisher.publish_message("", queue_name, "Hello World!")
    sleep(7)
    publisher.publish_message("", queue_name, "Hello World!")
