from array import array
from flask import Blueprint, request
from models.form import Form
from utils.db import db
from sqlalchemy import extract
import json
import ast

forms = Blueprint('forms', __name__)

@forms.route("/new/form", methods=['POST'])
def new_form():
    request_form = request.get_json()

    expansion = request_form['expansion']
    fecha = request_form['fecha']
    destino = request_form['destino']
    tonelaje = request_form['tonelaje']

    new_form = Form(expansion, fecha, destino, tonelaje)

    db.session.add(new_form)
    db.session.commit()

    return "New Form saved"

@forms.route("/filter/date", methods=['GET'])
def filter_date():
  dict_forms = {}
  lista_dict_forms = []
  
  mes = request.args.get('mes')
  año = request.args.get('año') 
  
  formsFilter = Form.query.filter(extract('year', Form.fecha)==año).filter(extract('month', Form.fecha)==mes).all()

  for row in formsFilter:
    dict_forms["id"] = row.id
    dict_forms["expansion"] = row.expansion
    dict_forms["fecha"] = str(row.fecha)
    dict_forms["destino"] = row.destino
    dict_forms["tonelaje"] = row.tonelaje
    lista_dict_forms.append(dict_forms.copy())

  return lista_dict_forms