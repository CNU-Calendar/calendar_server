from dataclasses import dataclass
import requests


@dataclass
class MovingMethods:
    name: str


WALK = MovingMethods("walk")
BUS = MovingMethods("bus")
CAR = MovingMethods("car")


class MapCalculator:
    def __init__(self, key):
        self._key: str = key
        self._minimum_time: int = -1
        self._path: list = []

    @property
    def minimum_time(self) -> int:
        assert self._minimum_time != -1, "minimum time is not calculated."
        return self._minimum_time

    @property
    def path(self) -> list:
        assert self._path, "Path is not exist."
        return self._path

    def get_path(self, start_coord: tuple[str, str], end_coord: tuple[str, str], start_name: str, end_name: str, method: MovingMethods) -> tuple:
        if method == WALK:
            url = "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1"

            headers = {'accept': 'application/json',
                       'content-type': 'application/json',
                       'appKey': self._key}

            payload = {"startX": start_coord[0],
                       "startY": start_coord[1],
                       "endX": end_coord[0],
                       "endY": end_coord[1],
                       "startName": start_name,
                       "endName": end_name,
                       "searchOption": "10",
                       "sort": "index"}

            res = requests.post(url=url, headers=headers, json=payload)

            if res.status_code == 200:
                data = dict(res.json())

                self._path = data["features"]
                self._minimum_time = data["features"][0]["properties"]["totalTime"]

                return self._path, self._minimum_time
            else:
                raise ValueError(f"get_path error! {res.status_code=}")
        elif method == BUS:
            url = "https://apis.openapi.sk.com/transit/routes"

            headers = {'accept': 'application/json',
                       'content-type': 'application/json',
                       'appKey': self._key}

            payload = {"startX": start_coord[0],
                       "startY": start_coord[1],
                       "endX": end_coord[0],
                       "endY": end_coord[1]}

            res = requests.post(url=url, headers=headers, json=payload)

            if res.status_code == 200:
                data = dict(res.json())
                self._path = data["metaData"]["plan"]["itineraries"][0]["legs"]
                self._minimum_time = data["metaData"]["plan"]["itineraries"][0]["totalTime"]

                return self._path, self._minimum_time
            else:
                raise ValueError(f"get_path error! {res.status_code=}")
        elif method == CAR:
            url = "https://apis.openapi.sk.com/tmap/routes?version=1"

            headers = {'accept': 'application/json',
                       'content-type': 'application/json',
                       'appKey': self._key}

            payload = {"startX": start_coord[0],
                       "startY": start_coord[1],
                       "endX": end_coord[0],
                       "endY": end_coord[1]}

            res = requests.post(url=url, headers=headers, json=payload)

            if res.status_code == 200:
                data = dict(res.json())
                self._path = data["features"]
                self._minimum_time = data["features"][0]["properties"]["totalTime"]

                return self._path, self._minimum_time
            else:
                raise ValueError(f"get_path error! {res.status_code=}")
        else:
            raise ValueError("method does not exist")
