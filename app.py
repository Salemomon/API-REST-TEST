from fastapi import FastAPI

query_db = [
    {
        "sucursal": "Pabellon",
        "Equipo":"Pabellon_01"
    },
    {
        "sucursal": "Pabellon",
        "Equipo":"Pabellon_04"
    },
    {
        "sucursal": "Pabellon",
        "Equipo":"Pabellon_03"
    },
    {
        "sucursal": "Pabellon",
        "Equipo":"Pabellon_02"
    },
    {
        "sucursal": "Pabellon",
        "Equipo":"Pabellon_05"
    }
]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Mensaje":"Bienvenido a tu api de prueba"}

@app.get("/equipos")
def get_equipos():
    return query_db

  