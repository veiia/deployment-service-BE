from pydantic import BaseModel


class ContainerCreationRequest(BaseModel):
    image: str
    owner_username: str
    project_dir_name: str


class ContainerUpdateRequest(BaseModel):
    image: str
    owner_username: str
    project_dir_name: str
