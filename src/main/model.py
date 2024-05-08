from pydantic import BaseModel


class GetPathItem(BaseModel):
    startX: str
    startY: str
    endX: str
    endY: str
    method: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "startX": "126.9246033",
                    "startY": "33.45241976",
                    "endX": "126.9041895",
                    "endY": "33.4048969",
                    "method": "walk"
                }
            ]
        }
    }


class Path(BaseModel):
    path: list
    min_time: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "path": ["a", "b", "c"],
                "min_time": 10
            }
        }
    }


class GetMinTimeItem(BaseModel):
    startX: str
    startY: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "startX": "126.9246033",
                "startY": "33.45241976"
            }
        }
    }


class Time(BaseModel):
    time: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "time": 10
            }
        }
    }


class User(BaseModel):
    id: str
    username: str


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str

