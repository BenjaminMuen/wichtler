from email.message import EmailMessage
from email.utils import formatdate, make_msgid

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

from typing import Optional

from core.models import Participant

from mail import templates


_env = Environment(loader=FileSystemLoader(templates.__path__), autoescape=select_autoescape(enabled_extensions=('html.h2'), default=False), undefined=StrictUndefined)

def build_message(p1: Participant, p2: Participant, title: str, url: Optional[str], sender: str, uuid: str) -> EmailMessage:
    context = {'giver': p1.name, 'receiver': p2.name, 'title': title, 'uuid': uuid, 'url': url or None}

    message = EmailMessage()

    message['Subject'] = title
    message['From'] = sender
    message['To'] = p1.email
    message['Date'] = formatdate(localtime=True)
    message['Message-ID'] = make_msgid()

    message.set_content(_env.get_template('wichteln.txt.j2').render(context))
    message.add_alternative(_env.get_template('wichteln.html.j2').render(context), subtype='html')

    return message