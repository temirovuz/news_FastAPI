from pydantic import BaseModel, EmailStr


class AuthorScheme(BaseModel):
    username: str
    email: EmailStr
    password: str

    # class Config:
    #     orm_mode = True


class AuthorViewScheme(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
