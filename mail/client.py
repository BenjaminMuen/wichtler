import smtplib

from email.message import EmailMessage

from .models import SmtpSettings

TIMEOUT = 30

def send_messages(settings: SmtpSettings, messages: list[EmailMessage]) -> None:
    with smtplib.SMTP_SSL(settings.host, settings.port, timeout=TIMEOUT) as smtp:
        smtp.login(settings.user, settings.password)

        for message in messages:
            smtp.send_message(message)
