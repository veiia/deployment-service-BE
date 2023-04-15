from app.clients.docker_client import DockerContainerManager
from app.concepts.container.models import Container, ContainerStatus, Logs
from app.concepts.container.requests import ContainerCreationRequest
from app.constants import CONTAINER_ID


manager = DockerContainerManager()


def create_container(request: ContainerCreationRequest) -> Container:
    image = request.image
    container_name = f"{request.owner_username}_{request.project_uuid}"
    container = manager.create_container(image=image, name=container_name)
    return Container(
        id=container.id,
        status=container.status,
        image=str(container.image),
        name=container.name,
        short_id=container.short_id,
    )


def delete_container(container_id: CONTAINER_ID) -> bool:
    return manager.delete_container(container_id)


def update_container(container_id: CONTAINER_ID):
    pass


def stop_container(container_id: CONTAINER_ID) -> ContainerStatus:
    status = manager.stop_container(container_id)
    return ContainerStatus(id=container_id, status=status)


def run_container(container_id: CONTAINER_ID) -> ContainerStatus:
    status = manager.run_container(container_id)
    return ContainerStatus(id=container_id, status=status)


def pause_container(container_id: CONTAINER_ID) -> ContainerStatus:
    status = manager.run_container(container_id)
    return ContainerStatus(id=container_id, status=status)


def get_info_about_container(container_id: CONTAINER_ID) -> dict:
    container_attrs = manager.get_info_about_container(container_id)
    return container_attrs


def get_status_of_container(container_id: CONTAINER_ID) -> ContainerStatus:
    status = manager.get_status_of_container(container_id)
    return ContainerStatus(id=container_id, status=status)


def get_logs_of_container(container_id: CONTAINER_ID, tail: int = 20) -> Logs:
    bytes_string_of_logs = manager.get_logs_of_container(container_id, tail)
    split_logs_by_lines = bytes_string_of_logs.decode("utf-8").split("\n")
    logs = [line for line in split_logs_by_lines]
    return Logs(id=container_id, logs=logs)


def kill_container(container_id: CONTAINER_ID) -> ContainerStatus:
    status = manager.kill_container(container_id)
    return ContainerStatus(id=container_id, status=status)
