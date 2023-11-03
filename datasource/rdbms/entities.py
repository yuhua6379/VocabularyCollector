from sqlalchemy import Column, String, Integer

from datasource.rdbms.base_entities import OrmBaseModel, Base


class WordModel(OrmBaseModel, Base):
    __tablename__ = "word"
    english_score = Column(Integer, nullable=False)
    worth_score = Column(Integer, nullable=False)
    usual_score = Column(Integer, nullable=False)

    english_reason = Column(String(10000), nullable=True, unique=False, default="")
    worth_reason = Column(String(10000), nullable=True, unique=False, default="")
    usual_reason = Column(String(10000), nullable=True, unique=False, default="")

    version = Column(String(200), nullable=True, unique=False, default="")

    pronounce = Column(String(200), nullable=True, unique=False, default="")
    meaning = Column(String(10000), nullable=True, unique=False, default="")
    examples = Column(String(10000), nullable=True, unique=False, default="")
    word = Column(String(100), nullable=True, unique=True, default="")

    prefix = Column(String(100), nullable=True, unique=False, default="")
