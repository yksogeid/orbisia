from flask import jsonify, request
from datetime import datetime
from collections import defaultdict
from app import db
from app.models import Mensaje

def guardar_mensaje(data):
    mensaje = Mensaje(
        telefono=data.get("telefono"),
        nombre=data.get("nombre"),
        pregunta=data.get("pregunta"),
        respuesta=data.get("respuesta"),
        horaMensajeRecibido=datetime.strptime(data.get("horaMensajeRecibido"), "%Y-%m-%d %H:%M:%S") if data.get("horaMensajeRecibido") else None,
        horaMensajeRespuesta=datetime.strptime(data.get("horaMensajeRespuesta"), "%Y-%m-%d %H:%M:%S") if data.get("horaMensajeRespuesta") else None,
    )
    db.session.add(mensaje)
    db.session.commit()
    return {"status": "ok", "recibido": data}

def obtener_conversaciones():
    mensajes = Mensaje.query.order_by(Mensaje.timestamp.asc()).all()
    resultado = [
        {
            "telefono": m.telefono,
            "nombre": m.nombre,
            "pregunta": m.pregunta,
            "respuesta": m.respuesta,
            "horaMensajeRecibido": m.horaMensajeRecibido.strftime("%H:%M") if m.horaMensajeRecibido else None,
            "horaMensajeRespuesta": m.horaMensajeRespuesta.strftime("%H:%M") if m.horaMensajeRespuesta else None,
            "timestamp": m.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        } for m in mensajes
    ]
    return resultado

def obtener_conversaciones_agrupadas():
    mensajes = Mensaje.query.order_by(Mensaje.timestamp.asc()).all()
    chats = defaultdict(list)
    for m in mensajes:
        chats[m.telefono].append({
            "telefono": m.telefono,
            "nombre": m.nombre,
            "pregunta": m.pregunta,
            "respuesta": m.respuesta,
            "horaMensajeRecibido": m.horaMensajeRecibido.strftime("%H:%M:%S") if m.horaMensajeRecibido else None,
            "horaMensajeRespuesta": m.horaMensajeRespuesta.strftime("%H:%M:%S") if m.horaMensajeRespuesta else None,
            "timestamp": m.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        })
    return chats
