from pydantic import BaseModel


class GetPath:
    class payload(BaseModel):
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

    class response(BaseModel):
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


class GetMinimumTime:
    class payload(BaseModel):
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

    class response(BaseModel):
        time: int

        model_config = {
            "json_schema_extra": {
                "example": {
                    "time": 10
                }
            }
        }


class SignUp:
    class payload(BaseModel):
        id: str
        username: str
        hashed_password: str

    class response(BaseModel):
        success: int


class SignIn:
    class payload(BaseModel):
        id: str
        hashed_password: str

    class response(BaseModel):
        access_token: str
        token_type: str


class SignOut:
    class payload(BaseModel):
        pass

    class response(BaseModel):
        pass
