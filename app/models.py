from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Configuration(Base):
    __tablename__ = 'configurations'
    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    business_name = Column(String)
    registration_number = Column(String)
    extra_details = Column(JSON)
