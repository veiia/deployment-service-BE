from fastapi import APIRouter
from fastapi.openapi.models import Response
from starlette import status

from app.concepts.container import actions
from app.concepts.container import responses
from app.concepts.container import requests
from app.constants import CONTAINER_ID

containers_router = APIRouter(prefix="/container", tags=["container"])


@containers_router.post("/", response_model=responses.ContainerIDResponse)
def create_container(request: requests.ContainerCreationRequest):
    _ = request
    container = actions.create_container()
    return container


@containers_router.delete("/{container_id}")
def delete_container(container_id: CONTAINER_ID):
    container = actions.delete_container(container_id=container_id)
    if container:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@containers_router.patch("/{container_id}", response_model=responses.ContainerResponse)
def update_container(
    container_id: CONTAINER_ID, request: requests.ContainerCreationRequest
):
    _ = request
    container = actions.update_container(container_id=container_id)
    if container:
        return container
    return Response(status_code=status.HTTP_404_NOT_FOUND)  # TODO ADD TO SWAGGER


@containers_router.post(
    "/{container_id}/stop", response_model=responses.ContainerStatusResponse
)
def stop_container(container_id: CONTAINER_ID):
    container_status = actions.stop_container(container_id=container_id)
    if container_status:
        return container_status
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@containers_router.post(
    "/{container_id}/run", response_model=responses.ContainerStatusResponse
)
def run_container(container_id: CONTAINER_ID):
    container_status = actions.run_container(container_id=container_id)
    if container_status:
        return container_status
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@containers_router.get(
    "/{container_id}/info", response_model=responses.ContainerResponse
)
def get_info_about_container(container_id: CONTAINER_ID):
    container = actions.get_info_about_container(container_id=container_id)
    if container:
        return container
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@containers_router.get(
    "/{container_id}/status", response_model=responses.ContainerStatusResponse
)
def get_status_of_container(container_id: CONTAINER_ID):
    container_status = actions.get_status_of_container(container_id=container_id)
    if container_status:
        return container_status
    return Response(status_code=status.HTTP_404_NOT_FOUND)
