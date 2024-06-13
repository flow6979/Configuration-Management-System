from pydantic import BaseModel
from typing import Optional, Dict

class ConfigurationBase(BaseModel):
    business_name: str
    registration_number: str
    extra_details: Dict

class ConfigurationCreate(ConfigurationBase):
    country_code: str

class ConfigurationUpdate(BaseModel):
    business_name: Optional[str] = None # none for allowing partial update
    registration_number: Optional[str] = None
    extra_details: Optional[Dict] = None


class Configuration(ConfigurationBase):
    id: int
    country_code: str

    class Config:
        from_attributes = True
