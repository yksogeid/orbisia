from flask import Blueprint, jsonify, request, render_template
from app.controllers.mensaje_controller import guardar_mensaje, obtener_conversaciones, obtener_conversaciones_agrupadas

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def index():
    return render_template("index.html")

@main_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    resultado = guardar_mensaje(data)
    return jsonify(resultado)

@main_bp.route('/conversaciones', methods=['GET'])
def conversaciones():
    return jsonify(obtener_conversaciones())

@main_bp.route('/conversaciones_agrupadas', methods=['GET'])
def conversaciones_agrupadas():
    return jsonify(obtener_conversaciones_agrupadas())
