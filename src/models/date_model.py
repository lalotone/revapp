from datetime import date, datetime
from pydantic import BaseModel, validator


class Date(BaseModel):
    dateOfBirth: date

    @validator('dateOfBirth', pre=True)
    def validate_date(cls, v):
        date_object = datetime.strptime(v, "%Y-%m-%d")
        if v.isalnum():
            raise ValueError("Invalid date format")
        if date_object.date() >= date.today():
            raise ValueError("Date is too recent")
        return v

