from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db, configuration)

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@router.patch("/update_configuration/{country_code}", response_model=schemas.Configuration)
def update_configuration(country_code: str, configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = crud.update_configuration(db, country_code, configuration)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@router.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.delete_configuration(db, country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration
