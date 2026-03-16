from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PatientBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    dni: str = Field(min_length=5, max_length=30)
    phone: str | None = Field(default=None, max_length=20)
    email: EmailStr | None = None


class PatientCreate(PatientBase):
    pass


class PatientUpdate(PatientBase):
    pass


class Patient(PatientBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DeleteResponse(BaseModel):
    message: str
