from flask import Blueprint, request
from models.form import Form
from utils.db import db

forms = Blueprint('forms', __name__)

@forms.route("/new/form", methods=['POST'])
def new_form():
    # expansion=request.form['expansion']
    # fecha=request.form['fecha']
    # destino=request.form['destino']
    # tonelaje=request.form['tonelaje']

    expansion= 'exp-llp4'
    fecha='2022-10-25'
    destino='Independencia-Santiago'
    tonelaje=2.83

    new_form = Form(expansion, fecha, destino, tonelaje)

    db.session.add(new_form)
    db.session.commit()

    return "New Form saved"

@forms.route("/filter/date")
def filter_date():
  return 'FIlter date'
