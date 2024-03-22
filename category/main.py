from fastapi import APIRouter

from category.scheme import CategoryViewScheme, CategoryScheme

app = APIRouter()


@app.post('/create_category')
def read_root(name: CategoryScheme):

    return name