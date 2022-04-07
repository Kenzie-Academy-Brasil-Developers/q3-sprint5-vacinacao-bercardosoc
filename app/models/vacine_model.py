from dataclasses import dataclass
from datetime import datetime, timedelta
import sqlalchemy.types as types 
from app.configs.database import db
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import validates

from app.exc.vaccine_exc import InvalidCPF

class TitleText(types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect) -> None:
        return value.title()

@dataclass
class VacineModel(db.Model):

    __tablename__ = "vaccine_cards"

    cpf: str = Column(String, primary_key=True)
    name: str = Column(TitleText, nullable=False)
    vaccine_name: str = Column(TitleText, nullable=False)
    health_unit_name: str = Column(TitleText)
    first_shot_date: str = Column(DateTime, default=datetime.now())
    second_shot_date: str = Column(DateTime, default=datetime.now() + timedelta(90))


    @validates("cpf")
    def validate_cpf(self, _, cpf_to_be_tested):
        if len(cpf_to_be_tested) != 11:
            raise InvalidCPF
        return cpf_to_be_tested