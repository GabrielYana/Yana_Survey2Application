from sqlmodel import Field , SQLModel

class ApplicantSchool(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    Username: str
    Password: str
    Fullname: str


