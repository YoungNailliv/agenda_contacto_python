class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "nombre":self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }
    
    def update(self,nombre, telefono, email):
        if nombre != "":
            self.nombre = nombre
        if telefono != "":
            self.telefono = telefono
        if email != "":
            self.email = email