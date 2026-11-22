from core.config import load_config, parse_settings, parse_participants
from core.draw import draw

from mail.models.smtp_settings import SmtpSettings
from mail.builder import build_message
from mail.client import send_messages

def main():
    smtp_settings = SmtpSettings.from_env()

    # parse config
    config = load_config('./config.json')

    title, url = parse_settings(config['settings'])
    participants = parse_participants(config['participants'])

    # draw matches
    matches = draw(participants)

    # generate messages
    messages = [build_message(p1, p2, title, url, smtp_settings.sender) for p1, p2 in matches.items()]

    # send messages
    send_messages(smtp_settings, messages)    

if __name__ == '__main__':
    main()