import enum

class PlanType(str, enum.Enum):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"