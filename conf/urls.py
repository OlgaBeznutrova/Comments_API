from django.urls import path
from django.contrib import admin

from fastapi import APIRouter

from comments.urls import router as comments_router

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = APIRouter()
router.include_router(comments_router)
