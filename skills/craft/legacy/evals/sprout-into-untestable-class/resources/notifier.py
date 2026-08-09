"""Outbound notification dispatch over SMTP."""

import smtplib
import time


class Notifier:
    """Sends transactional mail. One instance per worker process."""

    def __init__(self, host: str, port: int, sender: str) -> None:
        self._smtp = smtplib.SMTP(host, port, timeout=10)
        self._smtp.starttls()
        self._smtp.noop()
        self._sender = sender
        self._log: list[tuple[str, str, float]] = []

    def notify(self, recipient: str, subject: str, body: str) -> bool:
        """Send one message. Returns True when the gateway accepted it."""
        message = f"From: {self._sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
        refused = self._smtp.sendmail(self._sender, [recipient], message)
        self._log.append((recipient, subject, time.time()))
        return not refused

    def notify_batch(self, recipients: list[str], subject: str, body: str) -> int:
        """Send the same message to many recipients. Returns the accepted count."""
        return sum(1 for r in recipients if self.notify(r, subject, body))
