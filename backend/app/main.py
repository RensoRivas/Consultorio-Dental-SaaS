from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models
from .db import Base, engine, get_db

app = FastAPI(title="Consultorio Dental API", version="0.1.0")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


class PatientCreate(BaseModel):
    name: str
    email: str
    phone: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/login")
def login() -> dict[str, str]:
    return {"message": "Login endpoint pendiente de implementación"}


@app.get("/patients")
def list_patients(db: Session = Depends(get_db)) -> dict:
    patients = db.query(models.Patient).all()
    return {
        "items": [
            {
                "id": patient.id,
                "name": patient.name,
                "email": patient.email,
                "phone": patient.phone,
            }
            for patient in patients
        ]
    }


@app.post("/patients")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = models.Patient(
        name=patient.name,
        email=patient.email,
        phone=patient.phone,
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


@app.get("/appointments")
def list_appointments() -> dict:
    return {"items": []}