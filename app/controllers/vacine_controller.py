from http import HTTPStatus
from sqlite3 import IntegrityError
from click import MissingParameter
from sqlalchemy.exc import IntegrityError
from flask import request
from app.configs.database import db
from app.exc.vaccine_exc import InvalidCPF
from app.models.vacine_model import VacineModel
from app.vaccination_package.vaccination_services import validate_keys

def register_vacination():
    
    expected_keys = {"cpf", "name", "vaccine_name", "health_unit_name"}
    data = request.get_json()

    for value in list(data.values()):
        if type(value) != str:
            return {"error": "Values must be strings"}, HTTPStatus.BAD_REQUEST
            
    try: 
        validate_keys(data, expected_keys)
        card = VacineModel(**data)

        db.session.add(card)
        db.session.commit()

    except InvalidCPF:
        return {"error": "CPF must be 11 digits"}, HTTPStatus.BAD_REQUEST

    except MissingParameter as e:
        return e.args[0], HTTPStatus.BAD_REQUEST
    
    except KeyError as e:
        return e.args[0], HTTPStatus.BAD_REQUEST

    except IntegrityError as e:
         return {
             "error": "CPF already registered"
        }, HTTPStatus.CONFLICT

    return {
            "cpf": card.cpf,
            "name": card.name,
            "first_shot_date": card.first_shot_date,
            "second_shot_date": card.second_shot_date,
            "vaccine_name": card.vaccine_name,
            "health_unit_name": card.health_unit_name
        }, HTTPStatus.CREATED

def vacine_registers():
    vacine_data = (
        VacineModel
        .query
        .all()
    )

    serializer = [
        {
            "cpf": data.cpf,
            "name": data.name,
            "vaccine_name": data.vaccine_name,
            "health_unit_name": data.health_unit_name
        } for data in vacine_data
    ]
    return {"Vaccination data": serializer}, HTTPStatus.OK