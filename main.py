#Importando a classe flask do modulo jsonify para retornar o arquivo JSON
from flask import Flask, jsonify
#Importando o modulo JSON e os para obter total acesso ao arquivo 
import json
import os
#Importando uma extenção para habilitar o suporte CORS
from flask_cors import CORS

#Criando uma variavel para a classe flask e habilitando o suporte CORS
app = Flask(__name__)
CORS(app)

#Definindo a rota 
@app.route('/data')
def get_data():
    with open(os.path.realpath('places.json'), encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data)

#Criando uma condicional para verificar se o modulo esta sendo executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
#No terminal: pip install -r requirements.txt  
# Python .\main.py
