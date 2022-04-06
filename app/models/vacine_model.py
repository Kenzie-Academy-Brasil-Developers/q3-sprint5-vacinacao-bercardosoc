from dataclasses import dataclass
from datetime import datetime, timedelta
import sqlalchemy.types as types 
from app.configs.database import db
from sqlalchemy import Column, String, DateTime

class LowerCaseText(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect) -> None:
        return value.upper()

@dataclass
class VacineModel(db.Model):

    __tablename__ = "vaccine_cards"

    cpf: str = Column(String, primary_key=True)
    name: str = Column(LowerCaseText, nullable=False)
    vaccine_name: str = Column(LowerCaseText, nullable=False)
    health_unit_name: str = Column(LowerCaseText)
    first_shot_date: str = Column(DateTime, default=datetime.now())
    second_shot_date: str = Column(DateTime, default=datetime.now() + timedelta(90))


    