from fastapi import FastAPI


app = FastAPI()

@app.get('/blog')
def index(limit):
    return {'data':f'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'list of unpublished blogs'}

@app.get('/blog/{id}')
def get_id(id):
    return {'data': id}
