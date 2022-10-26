from ast import Try
from flask import Blueprint, request
from models.form import Form
from utils.db import db

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

@forms.route("/filter/date")
def filter_date():
  mes = request.args.get('mes')
  año = request.args.get('año') 
  formsFilter = Form.query(Form).filter(Form.fecha)
  return formsFilter
