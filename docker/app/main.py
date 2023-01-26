from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/connectpostgresql")
async def root():
    for i in range(retries):
        print('Connect attempt' + str(i))
        try:
            conn = psycopg2.connect("host=db dbname='postgres' user='postgres' password='postgres'")
            print('Connection successful')
            return {"message": "Connection to PostgreSQL successful"}
            break
        except psycopg2.OperationalError:
            print('Connection failed')
            sleep(delay)
            conn = None
            return {"message": "Not able to connect PostgreSQL"}
    
