from ..db import db
import os

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=True)
    stock = db.Column(db.Integer, unique = False, nullable=False)
    precio = db.Column(db.Float)
    parent_id = Column(db.Integer, ForeignKey("user.id"))
    user_favorite = db.relationship("Favorite_People", backref="Producto")

    def __repr__(self):
        return '<Producto %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "stock": self.stock,
            "precio": self.precio
        }
    
    