from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from category.scheme import CategoryViewScheme, CategoryScheme
from database.model import SessionLocal, Category

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create_category')
def read_root(category: CategoryScheme, db: Session = Depends(get_db)):
    print(category.name)
    new_category = Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
