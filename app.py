from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)    
    


#configuracion
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/basesnormales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.debug = True



class Pokemones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    elemnto =db.Column(db.String(128),nullable=False)
    hp = db.Column(db.Integer,nullable=False)
    atk = db.Column(db.Integer,nullable=False)
    deff = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(500),nullable=False)
    
    def __init__(self,name,elemnto,hp,atk,deff,description):
        self.name = name
        self.elemnto =elemnto
        self.hp =hp
        self.atk = atk
        self.deff =deff
        self.description =description
        

class PokemonesSchema(ma.Schema):
    class Meta:
        fields = ("id","name","elemnto","hp","atk","deff","description")
        
pokemon_schema = PokemonesSchema()
pokemones_schema = PokemonesSchema(many=True)
 


#adding a post
@app.route('/post', methods = ['POST'])
def add_pokemon():
    nombre = request.json['nombre']
    elemento = request.json['elemento']
    vida = request.json['vida']
    ataque = request.json['ataque']
    defensa = request.json['defensa']
    descripcion = request.json['descripcion']
 
    my_posts = Pokemones(nombre,elemento,vida,ataque,defensa,descripcion)
    db.session.add(my_posts)
    db.session.commit()
 
    return pokemon_schema.jsonify(my_posts)

#getting posts
@app.route('/get', methods = ['GET'])
def get_pokemones():
    all_pokemones = Pokemones.query.all()
    result = pokemones_schema.dump(all_pokemones)
 
    return jsonify(result)


#getting particular post
@app.route('/getById/<id>/', methods = ['GET'])
def pokemon_id(id):
    pokemon = Pokemones.query.get(id)
    return pokemon_schema.jsonify(pokemon)
 
 
#updating post
@app.route('/updateById/<id>/', methods = ['PUT'])
def pokemon_update(id):
    pokemon = Pokemones.query.get(id)
 
    nombre = request.json['nombre']
    elemento = request.json['elemento']
    vida = request.json['vida']
    ataque = request.json['ataque']
    defensa = request.json['defensa']
    descripcion = request.json['descripcion']
 
 
    pokemon.name = nombre
    pokemon.element = elemento
    pokemon.hp = vida
    pokemon.atk = ataque
    pokemon.deff = defensa
    pokemon.description = descripcion
    
    db.session.commit()
    return pokemon_schema.jsonify(pokemon)
 
 
 
#deleting post
@app.route('/deleteById/<id>/', methods = ['DELETE'])
def pokemon_delete(id):
    pokemon = Pokemones.query.get(id)
    db.session.delete(pokemon)
    db.session.commit()
 
    return pokemon_schema.jsonify(pokemon)
 