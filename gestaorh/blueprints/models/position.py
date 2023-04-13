from gestaorh.ext.database import db

class Position(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60))
	employeers = db.relationship('Employee', lazy='dynamic')


	def __repr__(self):
		return '<Position %r>' % self.id