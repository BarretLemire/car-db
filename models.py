from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    vin = Column(Text)
    model = Column(Text)
    make = Column(Text)
    engine = Column(Text)
    year = Column(Integer)

class Dealership(Base):
    __tablename__ = 'dealerships'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    address = Column(Text)
    phone_number = Column(Text)

class Inventory(Base):
    __tablename__ = 'inventory'

    car_id = Column(Integer, ForeignKey('cars.id'), primary_key=True)
    dealer_id = Column(Integer, ForeignKey('dealerships.id'), primary_key=True)
    cost = Column(Float)
    is_sold = Column(Boolean)

    car = relationship("Car")
    dealership = relationship("Dealership")
