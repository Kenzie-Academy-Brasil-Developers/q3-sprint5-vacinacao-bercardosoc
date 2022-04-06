from flask import Blueprint
from app.controllers.vacine_controller import register_vacination, vacine_registers

bp_vacine = Blueprint("bp_vacines", __name__, url_prefix="/vaccinations")

bp_vacine.post("")(register_vacination)
bp_vacine.get("")(vacine_registers)