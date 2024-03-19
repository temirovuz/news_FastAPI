from datetime import datetime

from sqlalchemy import Column, String, DateTime, BigInteger, ForeignKey, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

Base = declarative_base()
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Author(Base):
    __tablename__ = 'author'
    id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String(150), primary_key=True)
    email = Column(String)
    password = Column(String(50))

    news = relationship("News", back_populates="author")

    def __str__(self):
        return self.username


class Category(Base):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), unique=True)

    news = relationship("News", back_populates="categories")

    def __str__(self):
        return self.name


class News(Base):
    __tablename__ = 'news'
    id = Column(BigInteger, primary_key=True)
    title = Column(String)
    description = Column(String)
    # Category ForeignKey
    category_id = Column(BigInteger, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="news")
    # Author ForeignKey
    author_id = Column(BigInteger, ForeignKey('author.id'))
    author = relationship('Author', back_populates='news')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.title
