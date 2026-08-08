from device_registry import DeviceNotFound, DeviceRegistry

registry = DeviceRegistry()


def handle_device_revoked(device_id):
    """Called from a webhook. May fire more than once for the same device."""
    try:
        registry.unregister(device_id)
    except DeviceNotFound:
        pass


def handle_session_ended(device_ids):
    for device_id in device_ids:
        try:
            registry.unregister(device_id)
        except DeviceNotFound:
            pass


def device_status(device_id):
    try:
        info = registry.get(device_id)
        return {"status": "active", "info": info}
    except DeviceNotFound:
        return {"status": "inactive", "info": None}
