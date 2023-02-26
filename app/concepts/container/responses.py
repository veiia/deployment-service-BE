from pydantic import BaseModel

from app.constants import CONTAINER_ID


class ContainerIDResponse(BaseModel):
    id: CONTAINER_ID


class ContainerStatusResponse(ContainerIDResponse):
    status: str


class ContainerResponse(ContainerStatusResponse):
    # smth else
    ...
