import docker
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from app.concepts.manage import responses, actions, requests
from app.constants import CONTAINER_ID

manage_containers_router = APIRouter(
    prefix="/containers",
    # tags=['containers']
)


@manage_containers_router.get("", response_model=responses.ContainersListResponse)
def get_list_available_containers_for_user_view(username: str):  # TODO LIMIT OFFSET
    containers = actions.get_list_available_containers_for_user(username=username)
    return containers


@manage_containers_router.get(
    "/{container_id}", response_model=responses.ContainerResponse
)
def get_container_by_id_for_user_view(container_id: CONTAINER_ID):
    try:
        return actions.get_container_by_id_for_user(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@manage_containers_router.delete("/{container_id}")
def delete_container_by_id_for_user_view(container_id: CONTAINER_ID):
    try:
        # todo: написать правильные статус коды везде!!!!
        return actions.delete_container_by_id_for_user(container_id=container_id)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )


@manage_containers_router.post(
    "/reassign",
)
def reassign_all_containers_to_another_user_or_group_view(
    request: requests.ReassignContainersRequest,
):
    try:
        return actions.reassign_all_containers_to_another_user_or_group(request=request)
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Some of these containers are invalid."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@manage_containers_router.post(
    "/reassign/{container_id}", response_model=responses.ContainerResponse
)
def reassign_container_to_another_user_or_group_view(
    container_id: CONTAINER_ID, request: requests.ReassignContainerRequest
):
    try:
        return actions.reassign_container_to_another_user_or_group(
            container_id=container_id, request=request
        )
    except docker.errors.NotFound:
        return JSONResponse(
            content={"message": f"Container {container_id} Not Found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
