import json
import socket


class MetricsClient:
    """Client for the internal metrics collector."""

    def __init__(self):
        self._sock = None
        self._serializer = None
        self._buffer = []

    def connect(self, host="metrics.internal", port=8125):
        self._sock = socket.create_connection((host, port), timeout=2)

    def set_serializer(self, fmt):
        if fmt == "json":
            self._serializer = json.dumps
        else:
            raise ValueError(f"unsupported format: {fmt}")

    def send(self, event):
        if self._sock is None:
            raise RuntimeError("call connect() first")
        if self._serializer is None:
            raise RuntimeError("call set_serializer() first")
        self._buffer.append(self._serializer(event))

    def flush(self):
        for payload in self._buffer:
            self._sock.sendall(payload.encode() + b"\n")
        self._buffer = []

    def close(self):
        if self._sock:
            self._sock.close()
            self._sock = None
