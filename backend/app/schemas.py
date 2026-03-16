from datetime import date, datetime
from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date | None = None
    phone: str | None = None


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True


class AppointmentBase(BaseModel):
    patient_id: int
    starts_at: datetime
    reason: str | None = None


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int

    class Config:
        from_attributes = True
