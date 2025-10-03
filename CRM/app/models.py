from datetime import datetime
from app import db

class Mensaje(db.Model):
    __tablename__ = "mensajes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telefono = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(100), nullable=True)
    pregunta = db.Column(db.Text, nullable=True)
    respuesta = db.Column(db.Text, nullable=True)
    horaMensajeRecibido = db.Column(db.DateTime, nullable=True)
    horaMensajeRespuesta = db.Column(db.DateTime, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
