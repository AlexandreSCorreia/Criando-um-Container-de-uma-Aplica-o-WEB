import pyodbc 
from flask import Flask, request, jsonify, send_from_directory, url_for
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)

host=os.getenv('DB_HOST')
user=os.getenv('DB_USER')
password=os.getenv('DB_PASSWORD')
database=os.getenv('DB_NAME')

for driver in pyodbc.drivers():
   print(driver)

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            f'Server={host};' 
                            f'Database={database};' 
                            f'UID={user};' 
                            f'PWD={password};')
"""
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=localhost,1450;' 
                            'Database=FilmesDb;' 
                            'UID=SA;' 
                            'PWD=Numsey#2022;')
"""
lista_insert = [
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 1', 'Sinopse do Filme 1', '/static/images/capa1.jpg');",
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 2', 'Sinopse do Filme 2', '/static/images/capa2.jpg');",
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 3', 'Sinopse do Filme 3', '/static/images/capa3.jpg');",
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 4', 'Sinopse do Filme 4', '/static/images/capa4.jpg');",
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 5', 'Sinopse do Filme 5', '/static/images/capa5.jpg');",
    "INSERT INTO Filmes (nome, sinopse, imagem) VALUES ('Filme 6', 'Sinopse do Filme 6', '/static/images/capa6.jpg');"
]

for query in lista_insert:
    cursor = cnxn.cursor()
    cursor.execute(query) 


@app.route('/')
def index():
    cursor = cnxn.cursor()	
    cursor.execute("SELECT * FROM Filmes") 
    row = cursor.fetchone() 
    while row:
        print (row) 
        row = cursor.fetchone()
    return "Hello, World!"

@app.route('/filmes', methods=['GET'])
@cross_origin()
def listar_filmes():
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Filmes")
    filmes = cursor.fetchall()
    filmes_list = []
    for filme in filmes:
        print (filme) 
        filme_dict = {
            'id': filme[0],
            'nome': filme[1],
            'sinopse': filme[2],
            'imagem': filme[3]
        }
        filmes_list.append(filme_dict)
    return jsonify(filmes_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)