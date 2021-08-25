from sqlalchemy import Column, String, Integer, LargeBinary
from config.database import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(128), unique=True, nullable=False)
    password_hash = Column(LargeBinary, nullable=True)
    password_salt = Column(LargeBinary, nullable=True)
    token = Column(String(2048), nullable=False)

    def __repr__(self):
        return f'{self.email}'
