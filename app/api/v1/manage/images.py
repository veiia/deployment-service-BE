from fastapi import APIRouter
from fastapi.openapi.models import Response
from starlette import status

from app.concepts.manage import actions, responses
from app.constants import IMAGE_ID

manage_images_router = APIRouter(
    prefix="/images",
    # tags=['images']
)


@manage_images_router.get("", response_model=responses.ImagesListResponse)
def get_list_available_images_for_user_view():
    images = actions.get_list_available_images_for_user()
    # if user not found:
    #     return 404
    return images


@manage_images_router.get("/{image_id}", response_model=responses.ImageResponse)
def get_image_by_id_for_user_view(image_id: IMAGE_ID):
    image = actions.get_image_by_id_for_user(image_id=image_id)
    if image:
        return image
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_images_router.post("", response_model=responses.ImageResponse)
def create_image_for_user_view():
    is_success = actions.create_image_for_user()
    if is_success:
        return Response(status_code=status.HTTP_201_CREATED)
    return Response(status_code=status.HTTP_404_NOT_FOUND)


@manage_images_router.delete("/{image_id}")
def delete_image_by_id_for_user_view(image_id: IMAGE_ID):
    is_success = actions.delete_image_by_id_for_user(image_id=image_id)
    if is_success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)
