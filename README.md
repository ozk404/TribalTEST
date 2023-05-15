# 🐍 Flask - Tribal Test

Se debe desarrollar un API RESTful que contenga un único endpoint el cual retorne un array con un rango definido de 25 objetos, diferentes unos de otros, es decir no debe existir ningún objeto que contenga el mismo id.  los objetos será obtenidos de un API de terceros, teniendo como restricción consumir estrictamente el siguiente endpoint
https://api.chucknorris.io/jokes/random

## 💻 Instalación

Recomiendo utilizar un entorno virtual (virtualenv) para ejecturar este proyecto y no tener problemas de dependencias.
Para ejecutar el proyecto, es necesario clonar el repositorio:

```
git clone https://github.com/ozk404/TribalTEST
cd TribalTEST
python -m venv env
call env/scripts/activate
```

Despues, es necesario utilizar el gestor de paquetes de Python (PIP) [pip](https://pip.pypa.io/en/stable/) para instalar todas las dependencias y requerimientos necesarios para ejecutar el proyecto, estos se encuentran en el archivo "requirements.txt".

```
pip install -r requirements.txt
```

## 🚀 Iniciar el Proyecto
Una vez creado el entorno virtual, ejecutado e instaladas todas las dependencias y requerimientos, el proyecto puede ser ejecutado simplemente con la siguiente línea:
```
python endpoint.py 
```


## ⚙️ Uso:

```
localhost:5000
```

El sistema cuenta con 1 'Endpoint': 

| HTTP Type | Path | Used For |
| --- | --- | --- |
| `GET` | /chuck | Endpoint que retorna 25 resultados únicos del endpoint establecido|
