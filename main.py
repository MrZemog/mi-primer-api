from fastapi import FastAPI

app = FastAPI()

# Ruta raíz de prueba
@app.get("/")
def inicio():
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}

# Simulación del Smart Lookup para el ejercicio
@app.get("/buscar/{matricula}")
def buscar_alumno(matricula: str):
    if matricula == "12345":
        return {
            "nombre": "Juan Pérez",
            "carrera": "Ciencias Ambientales",
            "semestre": 5
        }
    return {"error": "Matrícula no encontrada"}
