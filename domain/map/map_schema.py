from pydantic import BaseModel, field_validator


class MapPath(BaseModel):
    start_x: str
    start_y: str
    end_x: str
    end_y: str
    method: str

    @field_validator('start_x', 'start_y', 'end_x', 'end_y', 'method')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Empty value is not allowed.')
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "start_x": "126.9246033",
                    "start_y": "33.45241976",
                    "end_x": "126.9041895",
                    "end_y": "33.4048969",
                    "method": "walk"
                }
            ]
        }
    }


class MapPathResponse(BaseModel):
    path: list
    min_time: int


class MapMinTime(BaseModel):
    start_x: str
    start_y: str

    @field_validator('start_x', 'start_y')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Empty value is not allowed.')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "start_x": "126.9246033",
                "start_y": "33.45241976"
            }
        }
    }


class MapMinTimeResponse(BaseModel):
    min_time: int
