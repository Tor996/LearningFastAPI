from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from models import AsyncSessionLocal
from crud import (add_doctor, get_doctors, get_single_doctor, update_doctor, delete_doctor,
                  add_patient, get_patients, get_single_patient, update_patient, delete_patient)
from schema import DoctorCreate, DoctorUpdate, DoctorRead, PatientCreate, PatientUpdate, PatientRead


app = FastAPI()


# Dependency to get the database session
async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Asynchronous Routes for Doctors
@app.post("/doctors/", response_model=DoctorRead)
async def create_doctor(doctor: DoctorCreate, db: AsyncSession = Depends(get_db)):
    return await add_doctor(db, doctor)


@app.get("/doctors/", response_model=List[DoctorRead])
async def read_doctors(db: AsyncSession = Depends(get_db)):
    return await get_doctors(db)


@app.get("/doctors/{doctor_id}", response_model=DoctorRead)
async def read_single_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    return await get_single_doctor(db, doctor_id)


@app.put("/doctors/{doctor_id}", response_model=DoctorRead)
async def update_doctor_data(doctor_id: int, doctor_data: DoctorUpdate, db: AsyncSession = Depends(get_db)):
    return await update_doctor(db, doctor_id, doctor_data)


@app.delete("/doctors/{doctor_id}")
async def remove_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_doctor(db, doctor_id)


# Asynchronous Routes for Patients
@app.post("/patients/", response_model=PatientRead)
async def create_patient(patient: PatientCreate, db: AsyncSession = Depends(get_db)):
    return await add_patient(db, patient)


@app.get("/patients/", response_model=List[PatientRead])
async def read_patients(db: AsyncSession = Depends(get_db)):
    return await get_patients(db)


@app.get("/patients/{patient_id}", response_model=PatientRead)
async def read_single_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    return await get_single_patient(db, patient_id)


@app.put("/patients/{patient_id}", response_model=PatientRead)
async def update_patient_data(patient_id: int, patient_data: PatientUpdate, db: AsyncSession = Depends(get_db)):
    return await update_patient(db, patient_id, patient_data)


@app.delete("/patients/{patient_id}")
async def remove_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_patient(db, patient_id)
