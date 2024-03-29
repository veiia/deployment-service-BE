from pydantic import BaseModel

from app.constants import CONTAINER_ID


class Image(BaseModel):
    pass


class ContainerID(BaseModel):
    id: CONTAINER_ID


class ContainerStatus(ContainerID):
    status: str
    # TODO: расширить модельку статуса (добавить isrunning is paused и тд)


class Container(ContainerStatus):
    image: str
    name: str
    short_id: str


class Logs(ContainerID):
    logs: list[str]
