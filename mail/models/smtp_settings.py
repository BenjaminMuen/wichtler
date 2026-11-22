import os

from dataclasses import dataclass
from dotenv import load_dotenv

from mail.utils import parse_int

@dataclass(frozen=True)
class SmtpSettings:
    host: str
    port: int
    user: str
    password: str
    sender: str

    @classmethod
    def from_env(cls) -> 'SmtpSettings':
        load_dotenv()

        host = os.getenv('SMTP_HOST')
        port = parse_int(os.getenv('SMTP_PORT', 465))
        user = os.getenv('SMTP_USER')
        password = os.getenv('SMTP_PASSWORD')
        sender = os.getenv('SMTP_SENDER')

        if not all((host, user, password, sender)):
            raise ValueError("Failed to parse SmtpSettings from env. Missing required environment variables: 'SMTP_HOST', 'SMTP_PORT', 'SMTP_USER', 'SMTP_PASSWORD' or 'SMTP_SENDER'.") from None

        return cls(host, port, user, password, sender)

    def __repr__(self) -> str:
        return f"SmtpSettings(host={self.server}, port={self.port}, user={self.user}, sender={self.sender})"