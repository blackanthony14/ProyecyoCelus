from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps
import datetime
import pandas as pd



app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)    
    


#configuracion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/ventaDeCelus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']= 'thisissecret'
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.debug = True

class Transacciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    telefono_id = db.Column(db.Integer,nullable=False)
    
    def __init__(self, user_id, telefono_id):
        self.user_id = user_id
        self.telefono_id = telefono_id
        

class TransaccionesSchema(ma.Schema):
    class Meta:
        fields = ("id","user_id","telefono_id")
        

transaccion_schema = TransaccionesSchema()
transacciones_schema = TransaccionesSchema(many=True)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), nullable=False)
    password =db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)
    
    def __init__(self, public_id, name, password, admin):
        self.public_id = public_id
        self.name = name
        self.password = password
        self.admin = admin 

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","public_id","name","password","admin")
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Telefono(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    marca = db.Column(db.String(200),nullable=False)
    imei =db.Column(db.String(200),nullable=False)
    precio = db.Column(db.Integer,nullable=False)
    ram = db.Column(db.String(100),nullable=False)
    pantalla = db.Column(db.String(100),nullable=False)
    gama = db.Column(db.String(100),nullable=False)
    sistemaOperativo = db.Column(db.String(200),nullable=False)
    espacionAlma = db.Column(db.String(100))
    aviable = db.Column(db.Boolean)
    
    def __init__(self,nombre, marca, imei, precio, ram, pantalla, gama,sistemaOperativo, espacionAlma,aviable):
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.precio = precio
        self.ram = ram 
        self.pantalla = pantalla
        self.gama = gama
        self.sistemaOperativo = sistemaOperativo
        self.espacionAlma = espacionAlma
        self.aviable = aviable

class TelefonoSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","marca","imei","precio","ram","pantalla","gama","sistemaOperativo","espacionAlma","aviable")
     
telefono_schema = TelefonoSchema()
telefonos_schema = TelefonoSchema(many=True)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated



@app.route('/Comprar/<id>/', methods = ['POST'])
@token_required
def telefono_compra(current_user,id):
    try:
        telefono = Telefono.query.get(id)
        usuario = User.query.filter_by(id = current_user.id)
        if (telefono is None):
            return jsonify({'message' : 'Telefono no existentee'})
        
        try:
            user_id = current_user.id
            telefono_id = id
            newtrans = Transacciones(user_id,telefono_id)
            db.session.add(newtrans)
            db.session.commit()
            return transaccion_schema.jsonify(newtrans)
        except Exception:
            return jsonify({'message' : 'Telefono no actualizado'})
    except Exception:
        return jsonify({'message' : 'Telefono no existente'})

@app.route('/Transacciones', methods = ['GET'])
@token_required
def transaccionesId(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    idUsuario = current_user.id
    trans = Transacciones.query.filter_by(user_id = idUsuario).all()
    return transacciones_schema.jsonify(trans)
        

@app.route('/sing in', methods = ['POST'])
def create_user():
    try:
        password = request.json['password']   
        name = request.json['name']
        hashed_password = generate_password_hash(password, method='sha256')
        password = hashed_password
        public_id = str(uuid.uuid4())
        admin = False

        new_user = User(public_id, name, password, admin)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message' : 'New user created!'})
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
 
 
#get
@app.route('/telefonos', methods = ['GET'])
@token_required
def get_item(current_user):
    all_item = Telefono.query.all()
    result = telefonos_schema.dump(all_item)
 
    return jsonify(result)

@app.route('/users', methods = ['GET'])
@token_required
def get_users(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    all_item = User.query.all()
    result = users_schema.dump(all_item)

    return jsonify(result)




@app.route('/telefonos/nombre', methods = ['GET'])
@token_required
def get_telefonobyNombre(current_user):
    try:
        nombre = request.json['nombre']    
        all_item = Telefono.query.filter_by(nombre = nombre).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})

@app.route('/telefonos/nombre/marca', methods = ['GET'])
@token_required
def get_telefonobyDynamic(current_user):
    try:
        nombre = request.json['nombre'] 
        marca = request.json['marca']    
        all_item = Telefono.query.filter_by(nombre = nombre,marca = marca).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})

@app.route('/telefonos/nombre/marca/gama', methods = ['GET'])
@token_required
def get_telefonobyDynamicc(current_user):
    try:
        nombre = request.json['nombre'] 
        marca = request.json['marca'] 
        gama = request.json['gama']    
        all_item = Telefono.query.filter_by(nombre = nombre,marca = marca, gama = gama).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})


@app.route('/telefonos/marca', methods = ['GET'])
@token_required
def get_telefonobyMarca(current_user):
    try:
        marca = request.json['marca']    
        all_item = Telefono.query.filter_by(marca = marca).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})
    

@app.route('/telefonos/marca/gama', methods = ['GET'])
@token_required
def get_telefonobyDynamiccc(current_user):
    try:
        marca = request.json['marca'] 
        gama = request.json['gama']    
        all_item = Telefono.query.filter_by(marca = marca,gama = gama).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})

@app.route('/telefonos/gama', methods = ['GET'])
@token_required
def get_telefonobyGama(current_user):
    try:
        gama = request.json['gama']    
        all_item = Telefono.query.filter_by(gama = gama).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})

@app.route('/telefonos/sistemaOperativo', methods = ['GET'])
@token_required
def get_telefonobySystem(current_user):
    try:
        sistemaOperativo = request.json['sistemaOperativo']    
        all_item = Telefono.query.filter_by(sistemaOperativo = sistemaOperativo).all()
        result = telefonos_schema.dump(all_item)
        return jsonify(result)
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})

@app.route('/Actualizar/<id>/', methods = ['PUT'])
@token_required
def telefono_update(current_user,id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    try:
        telefono = Telefono.query.get(id)
        if (telefono is None):
            return jsonify({'message' : 'Telefono no existente'})
        
        try:
            precio = request.json['precio']
            aviable = request.json['aviable']
            telefono.precio = precio
            telefono.aviable = aviable

            db.session.commit()
            return telefono_schema.jsonify(telefono)
        except Exception:
            return jsonify({'message' : 'Telefono no actualizado'})
    except Exception:
        return jsonify({'message' : 'Telefono no existente'})
    

@app.route('/AddPhone', methods = ['POST'])
@token_required
def create_telefono(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    try:
        nombre = request.json['nombre']   
        marca = request.json['marca']
        imei = request.json['imei']   
        precio = request.json['precio']
        ram = request.json['ram']   
        pantalla = request.json['pantalla']
        gama = request.json['imei']   
        sistemaOperativo = request.json['sistemaOperativo']
        espacionAlma = request.json['espacionAlma']   
        aviable = request.json['aviable']

        new_user = Telefono(nombre,marca,imei,precio,ram,pantalla,gama,sistemaOperativo,espacionAlma,aviable)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message' : 'New Telefono Added!'})
    except Exception:
        return jsonify({'message' : 'Mal ingreso de datos'})
    


@app.route('/DelPhones', methods = ['DELETE'])
@token_required
def deleteAll_telefonos(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    all_item = Telefono.query.all()
    result = telefonos_schema.dump(all_item)
    return jsonify(result)

@app.route('/DelPhone/<id>', methods = ['DELETE'])
@token_required
def delete_telefono(current_user,id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    try:
        telefono = Telefono.query.get(id)
        if (telefono is None):
            return jsonify({'message' : 'Telefono no existente'})
        
        try:
            db.session.delete(telefono)
            db.session.commit()
            return telefono_schema.jsonify(telefono)
        except Exception:
            return jsonify({'message' : 'Telefono no Borrado'})
    except Exception:
        return jsonify({'message' : 'Telefono no existente'})
    
