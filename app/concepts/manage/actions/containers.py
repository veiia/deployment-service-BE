from app.clients.docker_client import DockerContainerManager
from app.concepts.container.models import Container
from app.concepts.manage import requests
from app.concepts.manage.models import ContainersList
from app.constants import CONTAINER_ID

manager = DockerContainerManager()


def get_list_available_containers_for_user(username: str):
    # TODO: search by username
    containers = manager.get_list_of_containers(username=username)
    containers_list = []
    for container in containers:
        result = Container(
            id=container.id,
            status=container.status,
            image=str(container.image),
            name=container.name,
            short_id=container.short_id,
        )
        containers_list.append(result)
    return ContainersList(containers=containers_list)


def get_container_by_id_for_user(container_id: CONTAINER_ID) -> Container:
    container = manager.get_container(container_id=container_id)
    return Container(
        id=container.id,
        status=container.status,
        image=str(container.image),
        name=container.name,
        short_id=container.short_id,
    )


def delete_container_by_id_for_user(container_id: CONTAINER_ID):
    manager.stop_container(container_id)
    return manager.delete_container(container_id)


def reassign_all_containers_to_another_user_or_group(
    request: requests.ReassignContainersRequest,
) -> ContainersList:
    old_prefix = request.old_owner_username
    new_prefix = request.new_owner_username
    containers = []
    for container_id in request.containers_ids:
        container = manager.rename_container(container_id, old_prefix, new_prefix)
        result = Container(
            id=container.id,
            status=container.status,
            image=str(container.image),
            name=container.name,
            short_id=container.short_id,
        )
        containers.append(result)
    return ContainersList(containers=containers)


def reassign_container_to_another_user_or_group(
    container_id: CONTAINER_ID, request: requests.ReassignContainerRequest
) -> Container:
    old_prefix = request.old_owner_username
    new_prefix = request.new_owner_username
    container = manager.rename_container(container_id, old_prefix, new_prefix)
    return Container(
        id=container.id,
        status=container.status,
        image=str(container.image),
        name=container.name,
        short_id=container.short_id,
    )
