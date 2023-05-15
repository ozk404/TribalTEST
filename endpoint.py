from flask import Flask, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor
import itertools

app = Flask(__name__)

def consumir(url):
    endpoint = requests.get(url)
    endpoint_json = endpoint.json()
    return endpoint_json

@app.route('/chuck')
def consumir_chuck():
    url = "https://api.chucknorris.io/jokes/random"
    max_workers = 10  # Número de hilos a utilizar
    datos_vistos = set()  # Utilizamos un conjunto para almacenar los IDs únicos
    resultados = []
    
    
    # Nos aseguramos de que siempre sean 25 resultados.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while len(resultados) < 25:
            tareas = [executor.submit(consumir, url) for _ in range(max_workers)]
            resultados_parciales = [tarea.result() for tarea in tareas]

            for resultado in resultados_parciales:
                if resultado["id"] not in datos_vistos:
                    resultados.append(resultado)
                    datos_vistos.add(resultado["id"])
    
    return jsonify(resultados)

app.run(debug=True)