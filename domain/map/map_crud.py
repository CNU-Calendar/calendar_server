from fastapi import HTTPException
from starlette import status

from domain.map.map_schema import *

import requests
from env import APP_KEY


def get_path(map_path: MapPath) -> tuple[str, str]:
    if map_path.method == "walk":
        url = "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1"

        headers = {'accept': 'application/json',
                   'content-type': 'application/json',
                   'appKey': APP_KEY}

        payload = {"startX": map_path.start_x,
                   "startY": map_path.start_y,
                   "endX": map_path.end_x,
                   "endY": map_path.end_y,
                   "startName": "starrt",  # TODO
                   "endName": "ennd",
                   "searchOption": "10",
                   "sort": "index"}

        response = requests.post(url=url, headers=headers, json=payload)

        if response.status_code == 200:
            data = dict(response.json())
            path = data["features"]
            min_time = data["features"][0]["properties"]["totalTime"]

            return path, min_time
        else:
            print(f"get_path error {response.status_code=}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Get path failed{response.status_code}"
            )

    elif map_path.method == "bus":
        url = "https://apis.openapi.sk.com/transit/routes"

        headers = {'accept': 'application/json',
                   'content-type': 'application/json',
                   'appKey': APP_KEY}

        payload = {"startX": map_path.start_x,
                   "startY": map_path.start_y,
                   "endX": map_path.end_x,
                   "endY": map_path.end_y}

        response = requests.post(url=url, headers=headers, json=payload)

        if response.status_code == 200:
            data = dict(response.json())
            path = data["metaData"]["plan"]["itineraries"][0]["legs"]
            min_time = data["metaData"]["plan"]["itineraries"][0]["totalTime"]

            return path, min_time
        else:
            print(f"get_path error {response.status_code=}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Get path failed"
            )

    elif map_path.method == "car":
        url = "https://apis.openapi.sk.com/tmap/routes?version=1"

        headers = {'accept': 'application/json',
                   'content-type': 'application/json',
                   'appKey': APP_KEY}

        payload = {"startX": map_path.start_x,
                   "startY": map_path.start_y,
                   "endX": map_path.end_x,
                   "endY": map_path.end_y}

        response = requests.post(url=url, headers=headers, json=payload)

        if response.status_code == 200:
            data = dict(response.json())
            path = data["features"]
            min_time = data["features"][0]["properties"]["totalTime"]

            return path, min_time
        else:
            print(f"get_path error {response.status_code=}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Get path failed"
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Method does not exist"
        )


def get_min_time(map_min_time: MapMinTime) -> str:
    end_x = ...  # TODO get from database
    end_y = ...
    method = ...

    map_path = MapPath(
        start_x=map_min_time.start_x,
        start_y=map_min_time.start_y,
        end_x=end_x,
        end_y=end_y,
        method=method)

    if map_min_time.method in ("walk", "bus", "car"):
        _, min_time = get_path(map_path)
        return min_time

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Method does not exist"
        )
