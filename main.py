from fastapi import FastAPI

from category.main import app as app_category
from author.main import app as app_author
app = FastAPI()

app.include_router(app_category)
app.include_router(app_author)
