from gestaorh.ext.database import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	description = db.Column(db.String(200))
	password = db.Column(db.String(244))
