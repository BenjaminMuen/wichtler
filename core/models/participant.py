from dataclasses import dataclass


@dataclass
class Participant:
    name: str
    email: str

    @classmethod
    def from_record(cls, record: dict) -> "Participant":
        name = record.get('name')
        email = record.get('email')

        if not all((name, email)):
            raise ValueError(f"Failed to parse Participant. Missing required properties 'name' or 'email'.")

        return cls(name, email) 

    def to_record(self) -> dict:
        return {'name': self.name, 'email': self.email}

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Participant):
            return False

        return self.email == other.email