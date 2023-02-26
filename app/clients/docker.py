from app.constants import CONTAINER_ID


class DockerContainerManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def create_container(self):
        pass

    def delete_container(self, container_id: CONTAINER_ID):
        pass

    def update_container(self, container_id: CONTAINER_ID):
        pass

    def get_info_about_container(self, container_id: CONTAINER_ID):
        pass

    def get_status_of_container(self, container_id: CONTAINER_ID):
        pass

    def stop_container(self, container_id: CONTAINER_ID):
        pass

    def run_container(self, container_id: CONTAINER_ID):
        pass
