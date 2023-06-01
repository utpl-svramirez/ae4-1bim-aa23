"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.svramirez_ea4
coleccion = db.Paises

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Ecuador", "continente": "Americano", "habitantes (MM)": 17.8}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Colombia", "continente": "Americano", "habitantes (MM)": 51.52},
{"nombre": "China", "continente": "Asiático", "habitantes (MM)": 1412},
{"nombre": "Australia", "continente": "Oceanía", "habitantes (MM)": 17.8}
]

coleccion.insert_many(lista)