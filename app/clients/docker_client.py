import subprocess
from typing import Any

import docker
from app.constants import CONTAINER_ID


class DockerContainerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.client = docker.client.from_env()

    def get_list_of_containers(self, username: str) -> list[Any]:
        return self.client.containers.list()

    def create_container(self, image: str, name: str) -> CONTAINER_ID:
        try:
            self.client.images.get(image)
        except docker.errors.ImageNotFound:
            self.client.images.pull(image)
        container = self.client.containers.create(image=image, name=name)
        return container

    def delete_container(
        self, container_id: CONTAINER_ID, is_delete_volumes: bool = True
    ) -> bool:
        container = self.client.containers.get(container_id)
        container.remove(v=is_delete_volumes)
        try:
            container.reload()
            return False
        except docker.errors.NotFound:
            return True

    def update_container(self, container_id: CONTAINER_ID):
        cmd_string = f"docker build -d {container_id}"
        subprocess.run(cmd_string)

    def get_info_about_container(self, container_id: CONTAINER_ID) -> dict[Any, Any]:
        container = self.client.containers.get(container_id)
        return container.attrs

    def get_logs_of_container(self, container_id: CONTAINER_ID, tail: int):
        container = self.client.containers.get(container_id)
        return container.logs(tail=tail)

    def get_stats_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.stats()

    def get_status_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        return container.status

    def get_image_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        return container.image

    def stop_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.stop()
        container.reload()
        return container.status

    def pause_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.pause()
        container.reload()
        return container.status

    def run_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.start()
        container.reload()
        return container.status

    def kill_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.kill()
        container.reload()
        return container.status

    def rename_container(self, container_id: CONTAINER_ID, new_name: str):
        container = self.client.containers.get(container_id)
        container.rename(new_name)
        container.reload()
        return container
