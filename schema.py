from pydantic import BaseModel
from datetime import date


# Pydantic Model for Doctor
class DoctorCreate(BaseModel):
    first_name: str
    last_name: str
    special_interest: str
    email: str

    class Config:
        from_attributes = True


class DoctorUpdate(BaseModel):
    first_name: str
    last_name: str
    special_interest: str
    email: str

    class Config:
        from_attributes = True


class DoctorRead(DoctorCreate):
    id: int

    class Config:
        from_attributes = True


# Pydantic Model for Patient

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date

    class Config:
        from_attributes = True


class PatientUpdate(PatientCreate):
    pass

    class Config:
        from_attributes = True


class PatientRead(PatientCreate):
    id: int

    class Config:
        from_attributes = True
