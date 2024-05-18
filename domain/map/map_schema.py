from pydantic import BaseModel, field_validator


class MapPath(BaseModel):
    startX: str
    startY: str
    endX: str
    endY: str
    method: str

    @field_validator('startX', 'startY', 'endX', 'endY', 'method')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Empty value is not allowed.')
        return v
