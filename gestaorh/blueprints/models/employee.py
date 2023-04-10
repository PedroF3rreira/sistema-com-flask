from gestaorh.ext.database import db

class Employee(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String(60))
	base_salary = db.Column(db.Float())
	additional_salary = db.Column(db.Float())