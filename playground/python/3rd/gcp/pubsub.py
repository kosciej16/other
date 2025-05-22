import json
import logging
from time import sleep
from google.cloud import pubsub_v1
from threading import Thread


logging.basicConfig(level=logging.DEBUG)

proj_id = "theta-marking-348120"
topic = "kosciej-topic"
sub = "kosciej-topic-sub"
topic_name = "projects/{project_id}/topics/{topic}".format(
    project_id=proj_id,
    topic=topic,  # Set this to something appropriate.
)

# record = {"Key1": "Value1", "Key2": "Value2", "Key3": "Value3", "Key4": "Value4"}
record = {
    "interactionId": "0.5_0",
    "mailInfo": {"mailKind": "OPL2OPL", "fromDomain": "OPL", "toDomain": "Internal only", "mailType": "IsNew"},
    "metadata": {
        "From": "test@orange.pl",
        "FromDomain": "orange.pl",
        "To": ["test@gmail.com"],
        "ToDomains": ["gmail.com"],
        "CC": [],
        "CCDomains": [],
        "Subject": "Test",
        "SentDatetime": None,
    },
    "n_attachments": 0,
    "subject": "Test",
    "subject_clean": "Test",
    "content": "Gdzie obowiązuje alert? Ostrzeżenie otrzymali odbiorcy z 11 województw: \n    śląskiego, małopolskiego, dolnośląskiego, opolskiego, podkarpackiego, \n    świętokrzyskiego, lubelskiego, łódzkiego, mazowieckiego \n    (powiaty: białobrzeski, garwoliński, grójecki, kozienicki, lipski, \n    przysuski, Radom, radomski, szydłowiecki i zwoleński), lubuskiego (powiat wschowski) \n    ",
}


data = json.dumps(record).encode("utf-8")


def publish():
    publisher = pubsub_v1.PublisherClient()
    # publisher.create_topic(name=topic_name)
    topic_path = publisher.topic_path(proj_id, topic)
    print(topic_path)
    future = publisher.publish(topic_name, data)
    #
    res = future.result()
    print(res)


def subscribe(id_):
    subscription_name = "projects/{project_id}/subscriptions/{sub}".format(
        project_id=proj_id,
        # sub="projects/theta-marking-348120/subscriptions/kosciej-topic-sub",  # Set this to something appropriate.
        sub="kosciej-topic-sub",  # Set this to something appropriate.
    )

    def callback(message):
        print(id_, message.data.decode("utf-8"))
        print("SLEEPING")
        sleep(5)
        message.ack()

    with pubsub_v1.SubscriberClient() as subscriber:
        # subscriber.create_subscription(name=subscription_name, topic=topic_name)
        subscription_path = subscriber.subscription_path(proj_id, sub)
        print(subscription_path)
        # path = "projects/theta-marking-348120/topics/kosciej-topic"
        # subscription = subscriber.create_subscription(request={"name": subscription_path, "topic": path})
        # print(subscription)
        # return

        future = subscriber.subscribe(subscription_name, callback)
        future.result()
    # try:
    #     future.result()
    # except:
    #     pass
    # future.cancel()


def threads():
    t1 = Thread(target=subscribe, args=("ID1",))
    t2 = Thread(target=subscribe, args=("ID2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


publish()
# subscribe("ID2")
# while True:
#     sleep(10)
