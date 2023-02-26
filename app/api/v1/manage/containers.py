from fastapi import APIRouter
from fastapi.openapi.models import Response
from starlette import status

from app.concepts.manage import responses, actions
from app.constants import CONTAINER_ID

manage_containers_router = APIRouter(
    prefix="/containers",
    # tags=['containers']
)


@manage_containers_router.get("", response_model=responses.ContainersListResponse)
def get_list_available_containers_for_user_view():  # TODO LIMIT OFFSET
    # if user not found:
    #     return 404
    containers = actions.get_list_available_containers_for_user()
    return containers


@manage_containers_router.get(
    "/{container_id}", response_model=responses.ContainerResponse
)
def get_container_by_id_for_user_view(container_id: CONTAINER_ID):
    container = actions.get_container_by_id_for_user(container_id=container_id)
    if container:
        return container
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_containers_router.delete("/{container_id}")
def delete_container_by_id_for_user_view(container_id: CONTAINER_ID):
    is_success = actions.delete_container_by_id_for_user(container_id=container_id)
    if is_success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_containers_router.delete("/delete")
def delete_all_containers_for_user_view():
    is_success = actions.delete_all_containers_for_user()
    if is_success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_containers_router.post(
    "/reassign",
    # responses={
    #     201: {s}
    # },
)
def reassign_all_containers_to_another_user_or_group_view():
    is_success = actions.reassign_all_containers_to_another_user_or_group()
    if is_success:
        return Response(status_code=status.HTTP_201_CREATED)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_containers_router.post("/reassign/{container_id}")
def reassign_container_to_another_user_or_group_view(container_id: CONTAINER_ID):
    is_success = actions.reassign_container_to_another_user_or_group(
        container_id=container_id
    )
    if is_success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)
