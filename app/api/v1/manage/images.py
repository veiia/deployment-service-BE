from fastapi import APIRouter

manage_images_router = APIRouter(
    prefix='/images',
    # tags=['images']
)

IMAGE_ID = str


@manage_images_router.get('')
def get_list_available_images_for_user_view():
    pass


@manage_images_router.get('/{image_id}')
def get_image_by_id_for_user_view(image_id: IMAGE_ID):
    pass


@manage_images_router.delete('/{image_id}')
def delete_image_by_id_for_user_view(image_id: IMAGE_ID):
    pass


@manage_images_router.post('')
def create_image_for_user_view():
    pass


@manage_images_router.delete('')
def delete_all_images_for_user_view():
    pass
