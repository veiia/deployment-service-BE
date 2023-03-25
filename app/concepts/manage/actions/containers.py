from app.clients.docker_client import DockerContainerManager
from app.constants import CONTAINER_ID


def get_list_available_containers_for_user():
    client = DockerContainerManager()
    return client.get_list_of_containers()


def get_container_by_id_for_user(container_id: CONTAINER_ID):
    pass


def delete_container_by_id_for_user(container_id: CONTAINER_ID):
    pass


def delete_all_containers_for_user():
    pass


def reassign_all_containers_to_another_user_or_group():
    pass


def reassign_container_to_another_user_or_group(container_id: CONTAINER_ID):
    pass
