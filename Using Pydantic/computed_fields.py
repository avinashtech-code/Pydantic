from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
