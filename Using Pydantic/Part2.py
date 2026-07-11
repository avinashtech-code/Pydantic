from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: list[str]
contact_details: dict[str, Any] 
## another way contact_details: dict[str, str | int]


def insert_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight} kg")
    print(f"Married: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")
    print("PATIENT DATA INSERTED SUCCESSFULLY")


patient_info = {
    "name": "Nitish",
    "age": 30,
    "weight": 72.5,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "phone": "9876543210",
        "email": "nitish@gmail.com",
        "city": "Delhi"
    }
}

patient = Patient(**patient_info)

insert_patient_data(patient)
patient = Patient(**patient_info)

insert_patient_data(patient)
