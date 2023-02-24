from fastapi import APIRouter

manage_containers_router = APIRouter(
    prefix='/containers',
    # tags=['containers']
)

CONTAINER_ID = str


@manage_containers_router.get('')
def get_list_available_containers_for_user_view():
    pass


@manage_containers_router.get('/{container_id}')
def get_container_by_id_for_user_view(container_id: CONTAINER_ID):
    pass


@manage_containers_router.delete('/{container_id}')
def delete_container_by_id_for_user_view(container_id: CONTAINER_ID):
    pass


@manage_containers_router.delete('/create')
def delete_all_containers_for_user_view():
    pass


@manage_containers_router.post('/reassign')
def reassign_all_containers_to_another_user_or_group():
    pass


@manage_containers_router.post('/reassign/{container_id}')
def reassign_container_to_another_user_or_group():
    pass
