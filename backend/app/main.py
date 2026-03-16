from fastapi import FastAPI
from .db import Base, engine

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
def list_patients() -> dict[str, list]:
    return {"items": []}


@app.get("/appointments")
def list_appointments() -> dict[str, list]:
    return {"items": []}
