from pydantic import BaseModel


class CategoryScheme(BaseModel):
    name: str

    # class Config:
    #     orm_mode = True

class CategoryViewScheme(BaseModel):
    id: int
    name: str