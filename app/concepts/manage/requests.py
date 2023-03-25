from pydantic import BaseModel


class ReassignContainerRequest(BaseModel):
    old_owner_username: str
    new_owner_username: str
