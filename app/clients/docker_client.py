import subprocess
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

    def get_list_of_containers(self):
        return self.client.containers.list()

    def create_container(self) -> CONTAINER_ID:
        container = self.client.containers.create('nginx')
        return container

    def delete_container(self, container_id: CONTAINER_ID):
        container = self.client.get(container_id)
        container.remove()
        # cmd_string = f"docker rm {container_id}"
        # subprocess.run(cmd_string)

    def update_container(self, container_id: CONTAINER_ID):
        cmd_string = f"docker build -d {container_id}"
        subprocess.run(cmd_string)

    def get_info_about_container(self, container_id: CONTAINER_ID):
        # cmd_string = f"docker ps {container_id}"
        # subprocess.run(cmd_string)
        container = self.client.containers.get(container_id)
        return container.attrs

    def get_logs_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        return container.logs()

    def get_stats_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.start()

    def get_status_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        return container.status

    def get_image_of_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        return container.image

    def stop_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.stop()
        # cmd_string = f"docker stop {container_id}"
        # subprocess.run(cmd_string)

    def pause_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.pause()

    def run_container(self, container_id: CONTAINER_ID):
        container = self.client.containers.get(container_id)
        container.run()
        # cmd_string = f"docker run {container_id}"
        # subprocess.run(cmd_string)


if __name__ == "__main__":
    docker_client = DockerContainerManager()
    status = docker_client.get_status_of_container("1781fe434860")
    image = docker_client.get_image_of_container("1781fe434860")
    print(status, image)
    logs = docker_client.get_logs_of_container("1781fe434860")
    print(logs)
    info = docker_client.get_info_about_container("1781fe434860")
    print(info)
    created_container = docker_client.create_container()
    print(created_container.__dir__())
    created_container.start()
    print(docker_client.get_list_of_containers())
    # created_container_id = docker_client.create_container()
    # created_container_id = 'bbed64f225f3'
    # print(created_container_id)
    # created_container_info = docker_client.get_info_about_container(created_container_id)
    # print(created_container_info)
    # created_container_status = docker_client.get_status_of_container(created_container_id)
    # print(created_container_status)
    # created_container_is_stopped = docker_client.stop_container(created_container_id)
    # print(created_container_is_stopped)
    # created_container_is_run = docker_client.run_container(created_container_id)
    # print(created_container_is_run)
    # created_container_is_deleted = docker_client.delete_container(created_container_id)
    # print(created_container_is_deleted)