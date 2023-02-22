from flask import Flask, render_template, request, json, url_for,redirect, session
import os
import requests

app = Flask(__name__)

api_endereco = os.getenv('API_ENDE')
print(api_endereco)
api_porta = os.getenv('API_PORT')
print(api_porta)
api_url = f'http://{api_endereco}:{api_porta}'
print(api_url)

@app.route('/')
@app.route('/home')
def index():
    filmes = []

    try:
        response = requests.get(api_url+'/filmes')
        response.raise_for_status() # verifica se houve erro
        filmes = response.json()
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Erro de timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro ao realizar a requisição:", err)

    return render_template("index.html", data={"titulo": "NETFLIX CLONE", "filmes": filmes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)