from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from uvicorn import run
import json

import model
import map

PORT = 8000


with open("../../env/.json", "r") as f:
    data: dict = json.load(f)
key: str = data["appKey"]

app = FastAPI()


@app.post("/path", response_model=model.GetPath.response)
async def get_path(p: model.GetPath.payload) -> JSONResponse:
    map_calc = map.MapCalculator(key)

    start_coord = (p.startX, p.startY)
    end_coord = (p.endX, p.endY)

    start_name = "starrt"
    end_name = "ennd"

    path, time = map_calc.get_path(start_coord, end_coord, start_name, end_name, method=map.MovingMethods(p.method))

    path_time = model.GetPath.response(path=path, min_time=time)

    return JSONResponse(content=jsonable_encoder(path_time))


@app.post("/min_time", response_model=model.GetMinimumTime.response)
async def get_minimum_time(p: model.GetMinimumTime.payload) -> JSONResponse:
    """User Location + Server Location(도착 위치) -> min time"""
    time = model.GetMinimumTime.response(time=10)
    return JSONResponse(content=jsonable_encoder(time))


@app.post("/sign_up", response_model=model.SignUp.response)
async def sign_up(user: model.SignUp.payload) -> JSONResponse:
    # db에 유저 정보 추가
    pass


@app.post("/sign_in", response_model=model.SignIn.response)
async def sign_in(p: model.SignIn.payload) -> JSONResponse:
    # 만약 db에 유저가 있다면
    # jwt 토큰 발급

    # 성공 여부 리턴

    # 다른 post jwt valid 확인하기


    # 앱에서는 jwt토큰이 있는 경우 자동으로 로그인을 시도한다
    # 실패하면 로그인 화면으로 이동
    pass


@app.post("/sign_out", response_model=model.SignOut.response)
async def sign_out() -> JSONResponse:
    # jwt 토큰 폭파
    pass


if __name__ == "__main__":
    run(app, host="127.0.0.1", port=PORT)

# db 관련
# radis 관련
# 계정 관련
