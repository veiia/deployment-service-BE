import docker
from fastapi import APIRouter
from starlette import status
from starlette.responses import Response, JSONResponse

from app.concepts.container import actions
from app.concepts.container import responses
from app.concepts.container import requests
from app.constants import CONTAINER_ID

containers_router = APIRouter(prefix="/container", tags=["container"])


@containers_router.post("", response_model=responses.ContainerResponse)
def create_container(request: requests.ContainerCreationRequest):
    # TODO: ДОДЕЛАТЬ ПОДТЯГИВАНИЕ ЛЮБЫХ ОБРАЗОВ
    container = actions.create_container(image=request.image)
    return container


@containers_router.delete("/{container_id}")
def delete_container(container_id: CONTAINER_ID):
    try:
        is_deleted = actions.delete_container(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )
    if is_deleted:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_400_BAD_REQUEST)


@containers_router.patch("/{container_id}", response_model=responses.ContainerResponse)
def update_container(
    container_id: CONTAINER_ID, request: requests.ContainerCreationRequest
):
    # TODO: ДОДЕЛАТЬ АПДЕЙТ
    _ = request
    container = actions.update_container(container_id=container_id)
    if container:
        return container
    return Response(status_code=status.HTTP_404_NOT_FOUND)  # TODO ADD TO SWAGGER


@containers_router.post(
    "/{container_id}/stop", response_model=responses.ContainerStatusResponse
)
def stop_container(container_id: CONTAINER_ID):
    try:
        return actions.stop_container(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@containers_router.post(
    "/{container_id}/run", response_model=responses.ContainerStatusResponse
)
def run_container(container_id: CONTAINER_ID):
    try:
        return actions.run_container(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@containers_router.post(
    "/{container_id}/pause", response_model=responses.ContainerStatusResponse
)
def pause_container(container_id: CONTAINER_ID):
    try:
        return actions.pause_container(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@containers_router.get(
    "/{container_id}/info", response_model=responses.ContainerResponse
)
def get_info_about_container(container_id: CONTAINER_ID):
    try:
        container_attrs = actions.get_info_about_container(container_id=container_id)
        return JSONResponse(
            content=container_attrs, status_code=status.HTTP_200_OK
        )
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@containers_router.get(
    "/{container_id}/status", response_model=responses.ContainerStatusResponse
)
def get_status_of_container(container_id: CONTAINER_ID):
    try:
        return actions.get_status_of_container(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )


@containers_router.get(
    "/{container_id}/logs", response_model=responses.LogsResponse
)
def get_status_of_container(container_id: CONTAINER_ID, tail: int = 20):
    try:
        return actions.get_logs_of_container(container_id=container_id, tail=tail)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"}, status_code=status.HTTP_404_NOT_FOUND
        )
