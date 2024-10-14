from fastapi import APIRouter
from routers.v1 import region_router, city_router

router = APIRouter(prefix="/api/v1")

router.include_router(region_router)
router.include_router(city_router)
