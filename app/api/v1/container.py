from fastapi import APIRouter

containers_router = APIRouter(
    prefix='/container',
    tags=['container']
)

CONTAINER_ID = str


@containers_router.post('/{container_id}')
def create_container(container_id: CONTAINER_ID):
    pass


@containers_router.delete('/{container_id}')
def delete_container(container_id: CONTAINER_ID):
    pass


@containers_router.patch('/{container_id}')
def update_container(container_id: CONTAINER_ID):
    pass


@containers_router.post('/{container_id}/stop')
def stop_container(container_id: CONTAINER_ID):
    pass


@containers_router.post('/{container_id}/run')
def run_container(container_id: CONTAINER_ID):
    pass


@containers_router.get('/{container_id}/info')
def get_info_about_container(container_id: CONTAINER_ID):
    pass


@containers_router.get('/{container_id}/status')
def get_status_of_container(container_id: CONTAINER_ID):
    pass
