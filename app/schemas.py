from datetime import datetime

from pydantic import BaseModel, Field


class ServiceIn(BaseModel):
    slug: str = Field(min_length=1, max_length=120)
    owner: str
    env: str
    status: str = "healthy"


class ServiceOut(ServiceIn):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
