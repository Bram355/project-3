from sqlalchemy.orm import relationship
from freelance_manager.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Float

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    invoice = relationship("freelance_manager.models.invoice.Invoice", back_populates="payments")
