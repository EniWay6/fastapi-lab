from fastapi import APIRouter

from src.external_api.service import CatService

router = APIRouter(prefix="/cats", tags=["Cats"])
service = CatService()


@router.get("/random")
async def get_cat_fact():
    return await service.get_fact()
