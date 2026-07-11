from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


## toh multiple functions bnaa sakte hai without individualing doing the validation

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("INSERTED")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("UPDATED")


patient_info = {
    'name': 'nitish',
    'age': 30
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

update_patient_data(patient1)


update_patient_data(updated_patient)
