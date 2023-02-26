from pydantic import BaseModel

from app.constants import CONTAINER_ID


class ContainerID(BaseModel):
    id: CONTAINER_ID


class ContainerStatus(ContainerID):
    status: str


class ContainerResponse(ContainerStatus):
    # smth else
    ...
