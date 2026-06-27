from flask import Blueprint, request, jsonify
from database import get_connection

events_bp = Blueprint("events", __name__, url_prefix="/events")

#Rota para listar os eventos
@events_bp.route("/", methods=["GET"])
def get_events():
    conn = get_connection()
    events = conn.execute("SELECT * FROM events").fetchall()
    conn.close()
    return jsonify([dict(e) for e in events])

#Rota para buscar evento por id

#Rota para buscar evento por nome

#Rota para criar evento

#Rota para editar evento

#Rota para deletar evento
