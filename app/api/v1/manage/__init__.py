from fastapi import APIRouter

from .containers import manage_containers_router
from .images import manage_images_router

manage_router = APIRouter(prefix="/manage", tags=["manage"])

manage_router.include_router(manage_containers_router)
manage_router.include_router(manage_images_router)
