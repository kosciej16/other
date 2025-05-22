from queue import Queue
import threading
import time


def producer(queue):
    """Function that produces items and puts them in the queue"""
    for i in range(2):
        print(f"Producing item {i}")
        queue.put(i)
        time.sleep(1)


def consumer(queue):
    """Function that consumes items from the queue"""
    while True:
        item = queue.get()
        print(f"Consuming item {item}")
        # queue.task_done()


# Create a queue instance
q = Queue()

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,), daemon=True)

# Start the threads
# consumer_thread.start()
producer_thread.start()

# Wait for producer to finish
producer_thread.join()

# Wait for all items to be processed
q.join()
