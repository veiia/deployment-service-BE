from pydantic import BaseModel

from app.constants import CONTAINER_ID, IMAGE_ID


class ContainerIDResponse(BaseModel):
    id: CONTAINER_ID


class ContainerResponse(ContainerIDResponse):
    status: str
    image: str
    name: str
    short_id: str


class ContainersListResponse(BaseModel):
    containers: list[ContainerResponse]


class ImageResponse(BaseModel):
    id: IMAGE_ID


class ImagesListResponse(BaseModel):
    images: list[ImageResponse]
