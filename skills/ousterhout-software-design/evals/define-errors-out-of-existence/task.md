# Task: stop the DeviceNotFound crashes

Production keeps hitting unhandled `DeviceNotFound` errors from `DeviceRegistry`. Webhooks retry, sessions end twice, and new call sites regularly forget the try/except that the existing handlers use.

Clean this up so the crashes stop for good, including for future call sites that have not been written yet. Update `handlers.py` to match whatever you change.

## Expected behaviour

- Revoking or unregistering a device that is already gone is not an error.
- Checking the status of an unknown device reports it as inactive.
- Behavior of `register` is unchanged.
