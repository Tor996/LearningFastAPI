from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from models import Doctor, Patient
from schema import DoctorCreate, DoctorUpdate, PatientCreate, PatientUpdate
from typing import List, Union


# Asynchronous CRUD operations for Doctors
async def add_doctor(db: Session, doctor: DoctorCreate) -> Doctor:
    new_doctor = Doctor(**doctor.model_dump())
    db.add(new_doctor)
    await db.commit()
    await db.refresh(new_doctor)
    return new_doctor


async def get_doctors(db: Session):
    result = await db.execute(select(Doctor))
    return result.scalars().all()


async def get_single_doctor(db: Session, doctor_id: int):
    result = await db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = result.scalar()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


async def update_doctor(db: Session, doctor_id: int, doctor_data: DoctorUpdate):
    doctor = await get_single_doctor(db, doctor_id)
    for key, value in doctor_data.model_dump().items():
        setattr(doctor, key, value)
    await db.commit()
    await db.refresh(doctor)
    return doctor


async def delete_doctor(db: Session, doctor_id: int):
    doctor = await get_single_doctor(db, doctor_id)
    db.delete(doctor)
    await db.commit()
    return {"message": "Doctor deleted successfully"}


# Asynchronous CRUD operations for Patients
async def add_patient(db: Session, patient: PatientCreate) -> Patient:
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    await db.commit()
    await db.refresh(new_patient)
    return new_patient


async def get_patients(db: Session):
    result = await db.execute(select(Patient))
    return result.scalars().all()


async def get_single_patient(db: Session, patient_id: int):
    result = await db.execute(select(Patient).where(Patient.id == patient_id))
    patient = result.scalar()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


async def update_patient(db: Session, patient_id: int, patient_data: PatientUpdate):
    patient = await get_single_patient(db, patient_id)
    for key, value in patient_data.model_dump().items():
        setattr(patient, key, value)
    await db.commit()
    await db.refresh(patient)
    return patient


async def delete_patient(db: Session, patient_id: int):
    patient = await get_single_patient(db, patient_id)
    db.delete(patient)
    await db.commit()
    return {"message": "Patient deleted successfully"}

