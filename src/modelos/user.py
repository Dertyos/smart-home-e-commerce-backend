from ..db import db
import os


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    name = db.Column(db.String(60), unique=False, nullable=False)
    phone = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(250), unique= False, nullable=True)
    img_profile = db.Column(db.Text(), unique= False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    user_favorites = db.relationship("FavoritoProductos", backref="user")
    carritoCompras = db.relationship("CarritoCompras", backref="user")
    Compras = db.relationship("Compras", backref="user")
    problemas = db.relationship("Problemas", backref="user")
    reviews = db.relationship("Reviews", backref="user")
    estado = db.Column(db.String(60), nullable=False)
    


    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "img_profile": self.img_profile
            # do not. serialize the password, its a security breach
        }

