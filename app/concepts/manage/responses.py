from pydantic import BaseModel

from app.constants import CONTAINER_ID, IMAGE_ID


class ContainerResponse(BaseModel):
    container_id: CONTAINER_ID


class ContainersListResponse(BaseModel):
    containers: list[ContainerResponse]


class ImageResponse(BaseModel):
    image_id: IMAGE_ID


class ImagesListResponse(BaseModel):
    images: list[ImageResponse]
