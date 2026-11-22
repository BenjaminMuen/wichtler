import json

from typing import Optional

from .models import Participant

def load_config(file: str) -> dict:
    with open(file) as f:
        config = json.load(f)

    return config

def parse_participants(raw: dict) -> set[Participant]:
    participants = set()

    for participant_raw in raw:
        participant = Participant.from_record(participant_raw)

        participants.add(participant)

    return participants

def parse_title(raw: dict, fallback: str = 'Wichteln') -> Optional[str]:
    return raw.get('title', fallback)

def parse_url(raw: dict) -> Optional[str]:
    return raw.get('url', None)

def parse_settings(raw: dict) -> tuple[str, Optional[str]]:
    title = parse_title(raw)
    url = parse_url(raw)

    return title, url