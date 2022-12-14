from flask import Blueprint, request, abort
from models.form import Form
from utils.db import db
from sqlalchemy import extract

forms = Blueprint('forms', __name__)

@forms.route("/new/form", methods=['POST'])
def new_form():

  try:

    request_form = request.get_json()

    expansion = request_form['expansion']
    fecha = request_form['fecha']
    destino = request_form['destino']
    tonelaje = request_form['tonelaje']

    if expansion == '' or fecha == '' or destino == '' or tonelaje == '':
      return abort(400)

    new_form = Form(expansion, fecha, destino, tonelaje)

    db.session.add(new_form)
    db.session.commit()

    return "New Form saved"

  except:

    return abort(400)

@forms.route("/filter/date", methods=['GET'])
def filter_date():

  try:

    dict_forms = {}
    lista_dict_forms = []
    
    mes = request.args.get('mes')
    año = request.args.get('año') 
    
    if mes == '' or año == '':
      return abort(400)

    formsFilter = Form.query.filter(extract('year', Form.fecha)==año).filter(extract('month', Form.fecha)==mes).all()

    for row in formsFilter:
      dict_forms["id"] = row.id
      dict_forms["expansion"] = row.expansion
      dict_forms["fecha"] = str(row.fecha)
      dict_forms["destino"] = row.destino
      dict_forms["tonelaje"] = row.tonelaje
      lista_dict_forms.append(dict_forms.copy())

    return lista_dict_forms

  except:

    return abort(400)