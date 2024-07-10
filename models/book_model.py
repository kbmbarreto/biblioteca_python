from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class BookModel(settings.DATABASE_BaseModel):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(128))
    author: str = Column(String(128))
    year: int = Column(Integer)
    publishing_company_id = Column(Integer, ForeignKey('publishing_company.id'))
    readed: str = Column(Integer)
    digital: str = Column(Integer)
    physical: str = Column(Integer)
    cover: str = Column(String(256))

    # Relacionamento com a model de editoras
    publishing_company = relationship('PublishingCompanyModel', back_populates='books')
