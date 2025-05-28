from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from freelance_manager.database import Base

# Define valid statuses for invoices
INVOICE_STATUSES = ["pending", "paid", "overdue"]

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(String, default="pending")

    payments = relationship("Payment", back_populates="invoice")
    project = relationship("Project", back_populates="invoices")
