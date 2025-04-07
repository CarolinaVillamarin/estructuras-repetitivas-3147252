## Diccionarios :

## Son colecciones de datos
## Cada elemento en un diccionario
## se pueden dividir en dos partes 
# ## 1. clave : el nombre del elemento
# ## 2.valor : el valor del elemento
## Ejemplo de diccionario:
## Para caracterizar un pais:
Pais ={
    "nombre": "Colombia",
    "capital": "Bogota",
    "idioma": "Español",
    "poblacion": 51,
    "superficie": 1141748,
    "moneda": "peso colombiano", 
    "ciudades":[
        "Bogota",
        "Medellin",
        "Cali",
        "Barranquilla",
        "Cartagena"
    ]  
}


#acceder a propiedades:
print("capital de colombia:" , Pais ["capital"])
print("y se habla:" , Pais ["idioma"])
print("habitantes:" , Pais ["poblacion"])
print("y sus ciudades son :")
for ciudad in Pais ["ciudades"]:
    print(ciudad)
