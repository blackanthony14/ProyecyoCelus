from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)    
    


#configuracion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/registros'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.debug = True



class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    codigoId =db.Column(db.String(200),nullable=False)
    precio = db.Column(db.Integer,nullable=False)
    categoria = db.Column(db.String(200))
    fotografiaLink = db.Column(db.String(500))
    description = db.Column(db.String(500))
    anotacionG = db.Column(db.String(500))
    
    def __init__(self, nombre, codigoId, precio, categoria, fotografiaLink, description, anotacionG):
        self.nombre = nombre
        self.codigoId = codigoId
        self.precio = precio
        self.categoria = categoria 
        self.fotografiaLink = fotografiaLink
        self.description = description
        self.anotacionG = anotacionG

class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","codigoId","precio","categoria","fotografiaLink","description", "anotacionG")
 
        
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
 

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    codigoId =db.Column(db.String(200),nullable=False)
    puesto = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(200),)
    fotografia = db.Column(db.String(500))
    descripcion = db.Column(db.String(500))
    anotacionE = db.Column(db.String(500))
    
    def __init__(self, nombre, codigoId, puesto, rol, fotografia, descripcion, anotacionE):
        self.nombre = nombre
        self.codigoId = codigoId
        self.puesto = puesto
        self.rol = rol 
        self.fotografia = fotografia
        self.descripcion = descripcion
        self.anotacionE = anotacionE
        

class EmpleadoSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","codigoId","puesto","rol","fotografia","descripcion", "anotacionE")
        
empleado_schema = EmpleadoSchema()
empleados_schema = EmpleadoSchema(many=True)



#adding a post
@app.route('/item', methods = ['POST'])
def add_item():
    try:
        nombre = request.json['nombre']
        codigoId = request.json['codigoId']
        precio = request.json['precio']
        categoria = request.json['categoria']
        fotografiaLink = request.json['fotografiaLink']
        description = request.json['description']
        anotacionG = request.json['anotacionG']
        
    
        my_posts = Item(nombre,codigoId,precio,categoria,fotografiaLink,description,anotacionG)
        db.session.add(my_posts)
        db.session.commit()
    
        return item_schema.jsonify(my_posts)
    except Exception:
        s = "Es obligatorio llenar las casilla : nombre, codigoId y precio"
        return jsonify(s)

@app.route('/empleado', methods = ['POST'])
def add_empleado():
    try:
        nombre = request.json['nombre']
        codigoId = request.json['codigoId']
        puesto = request.json['puesto']
        rol = request.json['rol']
        fotografia = request.json['fotografia']
        descripcion = request.json['descripcion']
        anotacionE = request.json['anotacionE']
        
    
        my_posts = Empleado(nombre,codigoId,puesto,rol,fotografia,descripcion,anotacionE)
        db.session.add(my_posts)
        db.session.commit()
    
        return empleado_schema.jsonify(my_posts)
    except Exception:
        s = "Es obligatorio llenar las casilla : nombre, codigoId y puesto"
        return jsonify(s)



#getting posts
@app.route('/items', methods = ['GET'])
def get_item():
    all_item = Item.query.all()
    result = items_schema.dump(all_item)
 
    return jsonify(result)


@app.route('/empleados', methods = ['GET'])
def get_empleado():
    all_item = Empleado.query.all()
    result = empleados_schema.dump(all_item)
 
    return jsonify(result)




#getting particular post
@app.route('/item/<id>/', methods = ['GET'])
def item_id(id):
    try:
        item = Item.query.get(id)
        return item_schema.jsonify(item)
    except Exception:
        s = "El id no existe"
        return s.jsonify
    


@app.route('/empleado/<id>/', methods = ['GET'])
def empleado_id(id):
    try:
        empleado = Empleado.query.get(id)
        return empleado_schema.jsonify(empleado)
    except Exception:
        s = "El id no existe"
        return jsonify(s)
 
 
 
#updating post
@app.route('/item/<id>/', methods = ['PUT'])
def item_update(id):
    try:
        item = Item.query.get(id)
        if (item is None):
            sout = "Este item no existe"
            return jsonify(sout)
        try:
            nombre = request.json['nombre']
            codigoId = request.json['codigoId']
            precio = request.json['precio']
            categoria = request.json['categoria']
            fotografiaLink = request.json['fotografiaLink']
            description = request.json['description']


            item.nombre = nombre
            item.codigoId = codigoId
            item.precio = precio
            item.categoria = categoria
            item.fotografiaLink = fotografiaLink
    
            db.session.commit()
            return item_schema.jsonify(item)  
        except Exception:
            se = "Es obligatorio llenar las casilla : nombre, codigoId y precio"
            return jsonify(se)   
    except Exception:
        res = "El id no existe"
        return jsonify(res)  


@app.route('/empleado/<id>/', methods = ['PUT'])
def empleado_update(id):
    try:
        empleado = Empleado.query.get(id)
        if (empleado is None):
            sout = "Este empleado no existe"
            return jsonify(sout)
        
        try:
            nombre = request.json['nombre']
            codigoId = request.json['codigoId']
            puesto = request.json['puesto']
            rol = request.json['rol']
            fotografia = request.json['fotografia']
            descripcion = request.json['descripcion']


            empleado.nombre = nombre
            empleado.codigoId = codigoId
            empleado.puesto = puesto
            empleado.rol = rol
            empleado.fotografia = fotografia

            db.session.commit()
            return empleado_schema.jsonify(empleado)
        except Exception:
            s = "Es obligatorio llenar las casilla : nombre, codigoId y puesto"
            return jsonify(s) 
    except Exception:
        s = "El id no existe"
        return jsonify(s) 
 
 
 
 
#deleting post
@app.route('/item/<id>/', methods = ['DELETE'])
def item_delete(id):
    try:
        item = Item.query.get(id)
        db.session.delete(item)
        db.session.commit()
        return item_schema.jsonify(item)
    except Exception:
        s = "El id no existe"
        return jsonify(s) 
    

@app.route('/empleado/<id>/', methods = ['DELETE'])
def empleado_delete(id):
    try:
        empleado = Empleado.query.get(id)
        db.session.delete(empleado)
        db.session.commit()
        return empleado_schema.jsonify(empleado)
    except Exception:
        s = "El id no existe"
        return jsonify(s)    
 