from pydantic import BaseModel

class UserIDList(BaseModel):
    user_ids: list[int]
