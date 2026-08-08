from metrics_client import MetricsClient


def record_checkout(order):
    client = MetricsClient()
    client.connect()
    client.set_serializer("json")
    try:
        client.send({"event": "checkout", "order_id": order.id, "total": order.total})
        client.flush()
    finally:
        client.close()


def record_refund(order):
    client = MetricsClient()
    client.connect()
    client.set_serializer("json")
    try:
        client.send({"event": "refund", "order_id": order.id, "total": -order.total})
        client.flush()
    finally:
        client.close()
