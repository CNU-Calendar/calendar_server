from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.map import map_crud, map_schema

router = APIRouter(
    prefix="/api/map",
)


@router.post("/path", status_code=status.HTTP_200_OK)
def map_path(_map_path: map_schema.MapPath):
    return
