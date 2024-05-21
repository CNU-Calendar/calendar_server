from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.map import map_crud, map_schema

router = APIRouter(
    prefix="/api/map",
)


@router.post("/path", response_model=map_schema.MapPathResponse)
def map_path(_map_path: map_schema.MapPath):

    path, min_time = map_crud.get_path(_map_path)

    return {
        "path": path,
        "min_time": min_time
    }


@router.post("/min_time", response_model=map_schema.MapMinTimeResponse)
def map_min_time(_map_min_time: map_schema.MapMinTime):

    min_time = map_crud.get_min_time(_map_min_time)

    return {
        "min_time": min_time
    }
