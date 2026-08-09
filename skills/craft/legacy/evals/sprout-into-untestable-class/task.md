# Task: stop sending duplicate notifications

Support is getting complaints about duplicate emails. Add suppression to `notifier.py`: if the same recipient has already been sent the same subject within the last five minutes, skip the send and return False.

`Notifier` opens an SMTP connection in its constructor, and there is no test suite for this module.

## Expected behaviour

- A repeat of the same recipient and subject inside five minutes is not sent.
- The same recipient and subject after five minutes is sent normally.
- First-time sends and batch sends keep working.
