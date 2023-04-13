from gestaorh.ext.database import db
from .position import Position

class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(60))
	base_salary = db.Column(db.Float())
	additional_salary = db.Column(db.Float())
	position_id = db.Column(db.Integer, db.ForeignKey('position.id'), nullable=False)

	def __repr__(self):
		return self.full_name