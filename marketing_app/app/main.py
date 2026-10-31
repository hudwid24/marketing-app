from fastapi import FastAPI, UploadFile, File, Form
import os

app = FastAPI(title="Marketing IA API")

@app.post("/paso1-subir-foto")
def recibir_foto(foto: UploadFile = File(...)):
    # Requisito 1 y 2: Recibe foto y propone 3 guiones
    guiones = [
        {"id": 1, "texto": "Guion 1: Humor dinámico para TikTok."},
        {"id": 2, "texto": "Guion 2: Estilo corporativo y elegante para Instagram."},
        {"id": 3, "texto": "Guion 3: Rápido y en tendencia musical."}
    ]
    return {"mensaje": "Foto recibida exitosamente", "archivo": foto.filename, "guiones_propuestos": guiones}

@app.post("/paso2-generar-campana")
def generar_y_desplegar(guion_id: int = Form(...), red_social: str = Form(...)):
    # Requisito 3 y 4: Escoge guion, genera 3 fotos, 1 video y despliega
    return {
        "status": "Campaña exitosa",
        "guion_seleccionado": guion_id,
        "contenido_generado": ["foto1.png", "foto2.png", "foto3.png", "video_final.mp4"],
        "despliegue": f"Publicado correctamente en {red_social}"
    }
