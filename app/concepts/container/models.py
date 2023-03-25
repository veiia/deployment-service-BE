from pydantic import BaseModel

from app.constants import CONTAINER_ID


class Image(BaseModel):
    pass


class ContainerID(BaseModel):
    id: CONTAINER_ID


class ContainerStatus(ContainerID):
    status: str
    #todo расширить модельку статуса


class Container(ContainerStatus):
    image: str
    name: str
    short_id: str
