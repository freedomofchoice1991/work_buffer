from sqlalchemy.orm import relationship, mapped_column, DeclarativeBase, Mapped
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import Optional


# declarative base class
class Base(DeclarativeBase):
    pass


class Power(Base):
    __tablename__ = 'power'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    amount: Mapped[Optional[float]]
    date_time: Mapped[datetime]
    source_power_plant_id: Mapped[int] = mapped_column(ForeignKey('power_plant.id'))
    destination_power_plant_id: Mapped[int] = mapped_column(ForeignKey('power_plant.id'), nullable=True)
    data_source_id: Mapped[int] = mapped_column(ForeignKey('data_source.id'))

    source_power_plant = relationship("PowerPlant", foreign_keys=[source_power_plant_id])
    destination_power_plant = relationship("PowerPlant", foreign_keys=[destination_power_plant_id])

    def __eq__(self, other):
        is_the_same: bool = (self.date_time == other.date_time and
                             self.amount == other.amount and
                             self.source_power_plant_id == other.source_power_plant_id)
        return is_the_same


class PowerPlant(Base):
    __tablename__ = 'power_plant'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    power_plant_type: Mapped[str]
    production_status: Mapped[Optional[bool]]  # Produced or consumed
    renewable_energy_status: Mapped[Optional[bool]]  # renewable or conventional
    high_carbon_source_status: Mapped[Optional[bool]]  # high carbon or low carbon source category
    owner: Mapped[Optional[str]]
    location_id: Mapped[int] = mapped_column((ForeignKey('location.id')))
    emission_data = relationship("Emission", backref="power_plant")
    data_source_id: Mapped[int] = mapped_column(ForeignKey('data_source.id'))


class Emission(Base):
    __tablename__ = 'emission_data'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    emission_type: Mapped[str]
    emission_amount: Mapped[Optional[float]]
    calculation_method: Mapped[Optional[str]]
    data_estimation: Mapped[Optional[bool]]
    date_time: Mapped[datetime]
    power_plant_id: Mapped[int] = mapped_column(ForeignKey('power_plant.id'))
    data_source_id: Mapped[int] = mapped_column(ForeignKey('data_source.id'))

    def __eq__(self, other):
        is_the_same: bool = (self.date_time == other.date_time and
                             self.emission_amount == other.emission_amount and
                             self.data_estimation == other.data_estimation)
        return is_the_same


class Location(Base):
    __tablename__ = 'location'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    latitude: Mapped[Optional[float]]
    longitude: Mapped[Optional[float]]
    region: Mapped[Optional[str]]
    city: Mapped[Optional[str]]
    street: Mapped[Optional[str]]
    number: Mapped[Optional[int]]
    country_code: Mapped[Optional[str]]
    country_name: Mapped[Optional[str]]
    zip_code: Mapped[Optional[int]]
    power_plant = relationship("PowerPlant", backref="location")


class DataSource(Base):
    __tablename__ = 'data_source'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_source_name: Mapped[str]
    data_source_link: Mapped[str]
    power = relationship("Power", backref='data_source')
    power_plant = relationship("PowerPlant", backref='data_source')
    emission_data = relationship("Emission", backref='data_source')
