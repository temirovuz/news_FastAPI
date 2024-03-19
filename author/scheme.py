from pydantic import BaseModel


class AuthorScheme(BaseModel):
    username: str
    email: str
    password: str

    # class Config:
    #     orm_mode = True

