import random

from .models import Participant


def draw(participants: set[Participant]) -> dict[Participant, Participant]:
    n = len(participants)

    if n < 2:
        raise RuntimeError("Failed to draw. At least 2 Participants are required.")

    participants = list(participants)

    random.shuffle(participants)

    return {participants[i]: participants[(i + 1) % n] for i in range(n)}