from typing import Optional

from pydantic import BaseModel as SCBaseModel
from publishing_company_schema import PublishingCompanySchema


class BookSchema(SCBaseModel):
    id: Optional[int]
    title: str
    author: str
    year: int
    publishing_company_id: PublishingCompanySchema
    readed: str
    digital: str
    physical: str
    cover: str

    class Config:
        orm_mode = True
