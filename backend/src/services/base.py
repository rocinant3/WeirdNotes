from __future__ import annotations
from abc import ABCMeta, abstractmethod

from sqlalchemy.orm import Session

from config.database import Base


class BaseCRUD(metaclass=ABCMeta):

    @property
    @abstractmethod
    def model(self) -> Base:
        pass

    def __init__(self, db: Session):
        self.db = db

    def filter(self, first=False, **kwargs):
        query = self.db.query(self.model).filter_by(**kwargs)
        if first:
            return query.first()
        return query.all()

    def get(self, id: int) -> Base:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def all(self):
        return self.db.query(self.model).all()

    def create(self, data):
        obj = self.model(**data.dict())
        self.db.add(obj)
        self.db.commit()
        return obj

    def delete(self, id: int) -> None:
        self.db.query(self.model).filter(self.model.id == id).delete()
        self.db.commit()


class BaseService:
    pass
