from pydantic import BaseModel, field_validator

class UserInput(BaseModel):
    text: str

    @field_validator("text")
    def validate_text(cls, value):
        if len(value.strip()) == 0:
            raise ValueError("Input cannot be empty.")
        return value
