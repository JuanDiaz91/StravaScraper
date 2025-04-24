import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class UserProfile:
    id: int
    name: str
    location: str
    image_url: str
    description: Optional[str] = None

    def to_json(self, beauty: bool=True) -> str:
        return json.dumps(
            asdict(self),
            indent=4 if beauty else None,
            ensure_ascii=False
        )

    def to_dict(self) -> dict:
        return asdict(self)
