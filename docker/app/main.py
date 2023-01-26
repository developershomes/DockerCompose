from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/connectpostgresql")
async def root():
    return {"message": "Connection to PostgreSQL successful"}