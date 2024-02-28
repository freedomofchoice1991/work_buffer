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
    updated_at: Mapped[datetime]
    created_at: Mapped[datetime]
    emission_factor_type: Mapped[Optional[str]]
    is_estimated: Mapped[bool]
    estimation_method: Mapped[Optional[str]]

    def __init__(self, data: dict, **kw):
        super().__init__(**kw)
        self.zone = data.get('zone')
        self.carbon_intensity = data.get('carbonIntensity')
        self.date_time = datetime.strptime(data.get('datetime'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'datetime') else None
        self.updated_at = datetime.strptime(data.get('updatedAt'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'updatedAt') else None
        self.created_at = datetime.strptime(data.get('createdAt'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'createdAt') else None
        self.emission_factor_type = data.get('emissionFactorType')
        self.is_estimated = data.get('isEstimated')
        self.estimation_method = data.get('estimationMethod')


class PowerBreakdownResponse(Base):
    __tablename__ = 'power_breakdown_response'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    zone: Mapped[str]
    date_time: Mapped[datetime]
    updated_at: Mapped[datetime]
    created_at: Mapped[datetime]
    fossil_free_percentage: Mapped[int]
    renewable_percentage: Mapped[int]
    power_consumption_total: Mapped[int]
    power_production_total: Mapped[int]
    power_import_total: Mapped[int]
    power_export_total: Mapped[int]
    is_estimated: Mapped[bool]
    estimation_method: Mapped[Optional[str]]
    power_consumption_breakdown = relationship("PowerConsumptionBreakdown", backref="power_breakdown_response")
    power_production_breakdown = relationship("PowerProductionBreakdown", backref="power_breakdown_response")
    power_import_breakdown = relationship("PowerImportBreakdown", backref="power_breakdown_response")
    power_export_breakdown = relationship("PowerExportBreakdown", backref="power_breakdown_response")

    def __init__(self, data: dict, **kw):
        super().__init__(**kw)
        self.zone = data.get('zone')
        self.date_time = datetime.strptime(data.get('datetime'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'datetime') else None
        self.updated_at = datetime.strptime(data.get('updatedAt'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'updatedAt') else None
        self.created_at = datetime.strptime(data.get('createdAt'), '%Y-%m-%dT%H:%M:%S.%fZ') if data.get(
            'createdAt') else None
        self.fossil_free_percentage = data.get('fossilFreePercentage')
        self.renewable_percentage = data.get('renewablePercentage')
        self.power_consumption_total = data.get('powerConsumptionTotal')
        self.power_production_total = data.get('powerProductionTotal')
        self.power_import_total = data.get('powerImportTotal')
        self.power_export_total = data.get('powerExportTotal')
        self.is_estimated = data.get('isEstimated')
        self.estimation_method = data.get('estimationMethod')


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


class PowerImportBreakdown(Base):
    __tablename__ = 'power_import_breakdown'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    power_breakdown_response_id: Mapped[int] = mapped_column(ForeignKey('power_breakdown_response.id'))
    source: Mapped[str]
    value: Mapped[Optional[int]]


class PowerExportBreakdown(Base):
    __tablename__ = 'power_export_breakdown'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    power_breakdown_response_id: Mapped[int] = mapped_column(ForeignKey('power_breakdown_response.id'))
    source: Mapped[str]
    value: Mapped[Optional[int]]
