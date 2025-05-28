from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from freelance_manager.database import Base

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)

    projects = relationship("Project", back_populates="client")
