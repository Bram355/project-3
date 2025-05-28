from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from freelance_manager.database import Base



class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    client_id = Column(Integer, ForeignKey('clients.id')) 

    client = relationship("Client", back_populates="projects")


    client = relationship("Client", back_populates="projects")
    invoices = relationship("Invoice", back_populates="project")
    project = relationship("Project", back_populates="invoices")

