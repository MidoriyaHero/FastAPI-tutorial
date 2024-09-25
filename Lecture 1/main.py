from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/put")
async def put():
    return {"message": "this is put method"}


@app.get("/post")
async def post():
    return {"message": "this is post method"}


@app.get("/delete")
async def delete():
    return {"message": "this is delete method"}