class PredictionRequest(BaseModel):
    gender: str
    age: int
    academic_pressure: int = Field(alias='academic_pressure')
    cgpa: float
    study_satisfaction: int = Field(alias='study_satisfaction')
    sleep_duration: str = Field(alias='sleep_duration')
    dietary_habits: str = Field(alias='dietary_habits')
    suicidal_thoughts: str = Field(alias='suicidal_thoughts')
    work_study_hours: int = Field(alias='work_study_hours')
    financial_stress: int = Field(alias='financial_stress')
    family_history: str = Field(alias='family_history')