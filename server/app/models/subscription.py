from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from app.models.const.plan_type import PlanType
import enum

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(PlanType), unique=True, nullable=False)

    # Omnichannel limits
    max_channels = Column(Integer, nullable=False)
    max_monthly_usage = Column(Integer, nullable=False)

    price_cents = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    subscriptions = relationship("UserSubscription", back_populates="plan")