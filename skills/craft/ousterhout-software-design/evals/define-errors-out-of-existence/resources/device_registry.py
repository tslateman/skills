class DeviceNotFound(Exception):
    pass


class DeviceRegistry:
    """Tracks active devices per account."""

    def __init__(self):
        self._devices = {}

    def register(self, device_id, info):
        self._devices[device_id] = info

    def get(self, device_id):
        if device_id not in self._devices:
            raise DeviceNotFound(device_id)
        return self._devices[device_id]

    def unregister(self, device_id):
        if device_id not in self._devices:
            raise DeviceNotFound(device_id)
        del self._devices[device_id]
