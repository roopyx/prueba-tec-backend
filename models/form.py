from utils.db import db

class Form(db.model):
  id = db.Column(db.Integer, primary_key=True)
  expansion = db.Column(db.String(100))
  fecha = db.Column(db.Date)
  destino = db.Column(db.String(100))
  tonelaje = db.Column(db.Float)

  def __init__(self, expansion, fecha, destino, tonelaje):
    self.expansion = expansion
    self.fecha = fecha
    self.destino = destino
    self.tonelaje = tonelaje