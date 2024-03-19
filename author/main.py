from fastapi import APIRouter

app = APIRouter()

@app.get('/')
def read_root():
    return {'message': 'hello world'}