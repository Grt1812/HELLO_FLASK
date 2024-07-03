from flask import Flask, jsonify
#from flask_restful import Api, Resource
#from flask_sqlalchemy import SQLAlchemy
#from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
communes = {
    "Goma": ["kyeshero", "himbi 1", "himbi 2", "le volcan", "katindo",
              "carmel", "mapendo", "centre ville", "lac vert", "himbi 3",
              "murara", "kituku", "nyarubande", "ulpgl", "cclk",],
    "Karisimbi": ["Ndosho", "Katoyi", "Afia bora", "kantindo 2", "mabanga sud",
              "mabanga nord", "birere", "Turunga", "Mugunga"],
    
    }
@app.route('/communes/<ville>')
def get_communes(ville):
    
    if ville in communes:
        return jsonify(communes[ville])
    else:
        return jsonify({"error": "Ville non trouvée"}), 404

    if __name__ == '__main__':
        app.run(debug=True)


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///communes.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

# Configuration de Swagger
#SWAGGER_URL = '/swagger'
#API_URL = '/static/swagger.json'
#swaggerui_blueprint = get_swaggerui_blueprint(
    #SWAGGER_URL,
    #API_URL,
    #config={
        #'app_name': "Communes API"
    #}
#)
#app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

#api = Api(app)

#class Commune(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #ville = db.Column(db.String(80), nullable=False)
    #nom = db.Column(db.String(120), nullable=False)

    #def __repr__(self):
        #return f'<Commune {self.nom} de {self.ville}>'

#class CommunesResource(Resource):
    #"""
    #Endpoint pour gérer la liste des communes.
    #"""

   # def get(self):
       # """
        #Renvoie la liste de toutes les communes.
        #"""
        #communes = Commune.query.all()
        #return jsonify([{'ville': c.ville, 'nom': c.nom} for c in communes])

    #def post(self):
        #"""
        #Ajoute une nouvelle commune à la base de données.
       # """
        #data = request.get_json()
        #new_commune = Commune(ville=data['ville'], nom=data['nom'])
        #db.session.add(new_commune)
        #db.session.commit()
        #return jsonify({'message': 'Commune ajoutée avec succès'}), 201

#class CommuneResource(Resource):
   # """
    #Endpoint pour gérer une commune spécifique.
   # """

    #def get(self, ville, nom):
        #"""
        #Renvoie les informations d'une commune.
       # """
       # commune = Commune.query.filter_by(ville=ville, nom=nom).first()
        #if commune:
           # return jsonify({'ville': commune.ville, 'nom': commune.nom})
        #else:
            #return jsonify({'error': 'Commune non trouvée'}), 404

    #def delete(self, ville, nom):
        #"""
        #Supprime une commune de la base de données.
       # """
       # commune = Commune.query.filter_by(ville=ville, nom=nom).first()
       # if commune:
           # db.session.delete(commune)
           # db.session.commit()
            #return jsonify({'message': 'Commune supprimée avec succès'})
        #else:
            #return jsonify({'error': 'Commune non trouvée'}), 404

#api.add_resource(CommunesResource, '/communes')
#api.add_resource(CommuneResource, '/communes/<ville>/<nom>')

#if __name__ == '__main__':
    #db.create_all()
    #app.run(debug=True)



