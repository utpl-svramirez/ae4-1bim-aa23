"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.svramirez_ea4
coleccion = db.Ciudad

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Guayaquil", "provincia": "Guayas",
"región":"Costa", "zona": 8}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"nombre": "Quito", "provincia": "Pichincha", "región":"Sierra",
"zona": 3},
{"nombre": "Cuenca", "provincia": "Azuay", "región":"Sierra",
"zona": 3}
]

coleccion.insert_many(lista)