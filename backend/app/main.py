from fastapi import FastAPI
from .db import Base, engine

app = FastAPI(title="Consultorio Dental API", version="0.1.0")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/login")
def login() -> dict[str, str]:
    return {"message": "Login endpoint pendiente de implementación"}


@app.get("/patients")
def list_patients() -> dict[str, list]:
    return {"items": []}


@app.get("/appointments")
def list_appointments() -> dict[str, list]:
    return {"items": []}
