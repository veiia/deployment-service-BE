from app.clients.docker_client import DockerContainerManager
from app.concepts.container.models import Container
from app.concepts.manage import requests
from app.constants import CONTAINER_ID

manager = DockerContainerManager()


def get_list_available_containers_for_user(username: str):
    return manager.get_list_of_containers(username=username)


def get_container_by_id_for_user(container_id: CONTAINER_ID):
    pass


def delete_container_by_id_for_user(container_id: CONTAINER_ID):
    pass


def delete_all_containers_for_user():
    pass


def reassign_all_containers_to_another_user_or_group():
    pass


def reassign_container_to_another_user_or_group(
    container_id: CONTAINER_ID, request: requests.ReassignContainerRequest
):
    old_owner = request.old_owner_username
    new_owner = request.new_owner_username
    container = manager.rename_container(container_id, f"{new_owner}_{old_owner}")
    return Container(
        id=container.id,
        status=container.status,
        image=str(container.image),
        name=container.name,
        short_id=container.short_id,
    )
