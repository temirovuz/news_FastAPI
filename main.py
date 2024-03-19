from fastapi import FastAPI

from category.main import app as app_category

app = FastAPI()

app.include_router(app_category)
