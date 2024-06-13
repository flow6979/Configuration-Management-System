from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app import models, schemas
from fastapi import HTTPException


def get_configuration(db: Session, country_code: str):
    try:
        return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    try:
        db_configuration = models.Configuration(**configuration.dict())
        db.add(db_configuration)
        db.commit()
        db.refresh(db_configuration)
        return db_configuration
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    try:
        db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
        if db_configuration:
            for key, value in configuration.dict(exclude_unset=True).items():
                setattr(db_configuration, key, value)
            db.commit()
            db.refresh(db_configuration)
            return db_configuration
        raise HTTPException(status_code=404, detail="Configuration not found")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")

def delete_configuration(db: Session, country_code: str):
    try:
        db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
        if db_configuration:
            db.delete(db_configuration)
            db.commit()
            return db_configuration
        raise HTTPException(status_code=404, detail="Configuration not found")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
