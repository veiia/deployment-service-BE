from pydantic import BaseModel


class ContainerCreationRequest(BaseModel):
    image: str


class ContainerUpdateRequest(BaseModel):
    image: str
