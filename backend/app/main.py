from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from .db import Base, engine, get_db

app = FastAPI(title="Consultorio Dental API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/login")
def login() -> dict[str, str]:
    return {"message": "Login endpoint pendiente de implementación"}


@app.post("/patients", response_model=schemas.Patient, status_code=status.HTTP_201_CREATED)
def create_patient(payload: schemas.PatientCreate, db: Session = Depends(get_db)) -> models.Patient:
    existing_dni = db.query(models.Patient).filter(models.Patient.dni == payload.dni).first()
    if existing_dni:
        raise HTTPException(status_code=409, detail="Ya existe un paciente con ese DNI")

    if payload.email:
        existing_email = db.query(models.Patient).filter(models.Patient.email == str(payload.email)).first()
        if existing_email:
            raise HTTPException(status_code=409, detail="Ya existe un paciente con ese email")

    patient = models.Patient(
        first_name=payload.first_name,
        last_name=payload.last_name,
        dni=payload.dni,
        phone=payload.phone,
        email=str(payload.email) if payload.email else None,
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


@app.get("/patients", response_model=list[schemas.Patient])
def list_patients(db: Session = Depends(get_db)) -> list[models.Patient]:
    return db.query(models.Patient).order_by(models.Patient.created_at.desc()).all()


@app.get("/patients/{id}", response_model=schemas.Patient)
def get_patient(id: int, db: Session = Depends(get_db)) -> models.Patient:
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient


@app.put("/patients/{id}", response_model=schemas.Patient)
def update_patient(
    id: int,
    payload: schemas.PatientUpdate,
    db: Session = Depends(get_db),
) -> models.Patient:
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    existing_dni = (
        db.query(models.Patient)
        .filter(models.Patient.dni == payload.dni, models.Patient.id != id)
        .first()
    )
    if existing_dni:
        raise HTTPException(status_code=409, detail="Ya existe otro paciente con ese DNI")

    if payload.email:
        existing_email = (
            db.query(models.Patient)
            .filter(models.Patient.email == str(payload.email), models.Patient.id != id)
            .first()
        )
        if existing_email:
            raise HTTPException(status_code=409, detail="Ya existe otro paciente con ese email")

    patient.first_name = payload.first_name
    patient.last_name = payload.last_name
    patient.dni = payload.dni
    patient.phone = payload.phone
    patient.email = str(payload.email) if payload.email else None

    db.commit()
    db.refresh(patient)
    return patient


@app.delete("/patients/{id}", response_model=schemas.DeleteResponse)
def delete_patient(id: int, db: Session = Depends(get_db)) -> schemas.DeleteResponse:
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    db.delete(patient)
    db.commit()
    return schemas.DeleteResponse(message="Paciente eliminado correctamente")
