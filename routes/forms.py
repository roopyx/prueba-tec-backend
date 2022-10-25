from flask import Blueprint

forms = Blueprint('forms', __name__)

@forms.route("/new/form")
def new_form():
  return "New Form saved"

@forms.route("/filter/date")
def filter_date():
  return 'FIlter date'
