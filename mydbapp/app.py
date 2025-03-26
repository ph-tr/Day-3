from fastapi import FastAPI
from postgres import Postgres

app = FastAPI()
db = Postgres("postgres://postgres:abc123@db")

try:
    with db.get_cursor() as cursor:
        cursor.run("CREATE TABLE foo(bar TEXT, baz INT)")
        cursor.run("INSERT INTO foo VALUES ('buz', 42), ('bit', 537)")
except:
    ...

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/all")
def select_star():
    rows = db.all("SELECT * FROM foo")
    return rows