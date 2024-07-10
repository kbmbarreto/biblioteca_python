from typing import Optional

from pydantic import BaseModel as SCBaseModel


class PublishingCompanySchema(SCBaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True