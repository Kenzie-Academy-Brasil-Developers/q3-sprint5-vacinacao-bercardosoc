from dataclasses import dataclass
from datetime import datetime, timedelta
from email.policy import default
from app.configs.database import db
from sqlalchemy import Column, String, DateTime

class VacineModel(db.Model):

    __tablename__ = "vaccine_cards"

    cpf: str = Column(String(length=11), primary_key=True)
    name: str = Column(String(50), nullable=False)
    vaccine_name: str = Column(String(50), nullable=False)
    health_unit_name: str = Column(String(50))
    first_shot_date: str = Column(DateTime, default=datetime.now())
    second_shot_date: str = Column(DateTime, default=datetime.now() + timedelta(90))
