from pydantic import BaseModel

from app.constants import CONTAINER_ID


class ContainerIDResponse(BaseModel):
    id: CONTAINER_ID


class ContainerStatusResponse(ContainerIDResponse):
    status: str


class ContainerResponse(ContainerStatusResponse):
    image: str
    name: str
    short_id: str


class LogsResponse(ContainerIDResponse):
    logs: list[str]
