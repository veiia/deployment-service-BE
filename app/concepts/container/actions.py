from app.clients.docker_client import DockerContainerManager
from app.concepts.container.models import Container, ContainerStatus
from app.constants import CONTAINER_ID


manager = DockerContainerManager()


def create_container(image: str) -> Container:
    container = manager.create_container(image=image)
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


def get_info_about_container(container_id: CONTAINER_ID):
    container_attrs = manager.get_info_about_container(container_id)
    return container_attrs


def get_status_of_container(container_id: CONTAINER_ID):
    status = manager.get_status_of_container(container_id)
    return ContainerStatus(id=container_id, status=status)


def get_logs_of_container(container_id: CONTAINER_ID, tail: int = 20):
    status = manager.get_logs_of_container(container_id, tail)
    return ContainerStatus(id=container_id, status=status)
