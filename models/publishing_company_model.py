from core.configs import settings
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class PublishingCompanyModel(settings.DATABASE_BaseModel):
    __tablename__ = 'publishing_company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(128), unique=True, nullable=False)

    # Relacionamento com a model de livros
    books = relationship('BookModel', back_populates='publishing_company')
