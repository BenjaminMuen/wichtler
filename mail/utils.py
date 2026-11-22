from typing import Optional

def parse_int(raw, fallback: Optional[int] = None) -> Optional[int]:
    try:
        return int(raw)
    
    except ValueError:
        return fallback