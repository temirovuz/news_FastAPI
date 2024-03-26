from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from author.scheme import AuthorScheme, AuthorViewScheme
from database.model import SessionLocal, Author

app = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create_author')
def read_root(author: AuthorScheme, db: Session = Depends(get_db)):
    authors = Author(username=author.username, email=author.email, password=author.password)
    db.add(authors)
    db.commit()
    db.refresh(authors)
    return authors


@app.get('/read_author', response_model=AuthorViewScheme)
def read_author(db: Session = Depends(get_db)):
    author = db.query(Author).all()
    return author
