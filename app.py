#from flask import Flask, jsonify
#from flask_restful import Api, Resource
#from flask_sqlalchemy import SQLAlchemy
#from flask_swagger_ui import get_swaggerui_blueprint
import os
from supabase import create_client, Client
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

URL = 'https://fbvbqxphjgbrcnupaqss.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZidmJxeHBoamdicmNudXBhcXNzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk5OTk1MTQsImV4cCI6MjAzNTU3NTUxNH0.DjphLasvwmf9EBl4ZAmxdiorPKR1phe6-T4r-jqDYxs'
supabase: Client = create_client(URL, KEY)

API_KEY = "78dac4af814e88ddca23f94fdf832a95"

@app.route('/')
def index():
    return "Bienvenue à l'API météo !"

@app.route('/meteo/<ville>')
def get_meteo(ville):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + ville
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # Conversion de Kelvin en Celsius
        return jsonify({'ville': ville, 'temperature': round(temp_celsius, 2)})
    else:
        return jsonify({'error': 'Ville non trouvée'}), 404

@app.route('/communes/<ville>')
def get_communes(ville):
    response = (
        supabase.table("Ville")
        .select("communes")
        .eq("nom", ville)
        .execute()
    )

    if response.data:
        return jsonify({"communes": response.data[0]["communes"]})
    else:
        return jsonify({"error": "Ville non trouvée"}), 404

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



