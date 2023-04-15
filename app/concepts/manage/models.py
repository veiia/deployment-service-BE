from pydantic import BaseModel

from app.concepts.container.models import Container


class ContainersList(BaseModel):
    containers: list[Container]
