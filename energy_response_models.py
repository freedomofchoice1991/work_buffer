from sqlalchemy.orm import relationship, mapped_column, DeclarativeBase, Mapped
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import Optional


# declarative base class
class Base (DeclarativeBase):
    pass


class CarbonIntensityResponse(Base):
    __tablename__ = 'carbon_intensity_response'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    zone: Mapped[str]
    carbon_intensity: Mapped[Optional[int]]
    date_time: Mapped[datetime]

    def __init__(self, data: dict, **kw):
        super().__init__(**kw)
        self.zone = data.get('zone')
        self.carbon_intensity = data.get('carbonIntensity')
        self.date_time = datetime.strptime(data.get('datetime'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'datetime') else None


class PowerBreakdownResponse(Base):
    __tablename__ = 'power_breakdown_response'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    zone: Mapped[str]
    date_time: Mapped[datetime]
    power_consumption_breakdown = relationship("PowerConsumptionBreakdown", backref="power_breakdown_response")
    power_production_breakdown = relationship("PowerProductionBreakdown", backref="power_breakdown_response")

    def __init__(self, data: dict, **kw):
        super().__init__(**kw)
        self.zone = data.get('zone')
        self.date_time = datetime.strptime(data.get('datetime'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'datetime') else None


class PowerConsumptionBreakdown(Base):
    __tablename__ = 'power_consumption_breakdown'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    power_breakdown_response_id: Mapped[int] = mapped_column(ForeignKey('power_breakdown_response.id'))
    source: Mapped[str]
    value: Mapped[Optional[int]]


class PowerProductionBreakdown(Base):
    __tablename__ = 'power_production_breakdown'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    power_breakdown_response_id: Mapped[int] = mapped_column(ForeignKey('power_breakdown_response.id'))
    source: Mapped[str]
    value: Mapped[Optional[int]]
