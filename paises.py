paises = [
    {
        "nombre": "Colombia",
        "poblacion": 50372424,
        "capital": "Bogotá",
        "idioma": "Español",
        "moneda": "Peso colombiano",
        "ciudades": [
            {
                "nombre": "Medellín",
                "poblacion": 2500000,
                "superficie": 382,
                "fundacion": 1616,
            },
            {
                "nombre": "Cali",
                "poblacion": 2400000,
                "superficie": 560,
                "fundacion": 1536,
            },
            {
                "nombre": "Barranquilla",
                "poblacion": 1200000,
                "superficie": 150,
                "fundacion": 1629,
            },
            {
                "nombre": "Cartagena",
                "poblacion": 1000000,
                "superficie": 572,
                "fundacion": 1533,
            },
        ],
    },
    {
        "nombre": "Perú",
        "capital": "Lima",
        "idioma": "Español",
        "moneda": "Sol",
        "ciudades": [
            {"nombre": "Lima", "poblacion": 9674755, "fundacion": 1535},
            {"nombre": "Arequipa", "poblacion": 1008290, "fundacion": 1540},
            {"nombre": "Cusco", "poblacion": 428450, "fundacion": 1100},
        ],
    },
    {
        "nombre": "Guayana Francesa",
        "capital": "Cayena",
        "idioma": "Francés",
        "moneda": "Euro",
        "ciudades": [
            {"nombre": "Cayena", "poblacion": 61000, "fundacion": 1643},
            {
                "nombre": "Kourou",
                "poblacion": 26000,
                "superficie": 1500,
                "fundacion": 1720,
            },
            {
                "nombre": "Saint-Laurent-du-Maroni",
                "superficie": 2000,
                "poblacion": 45000,
                "fundacion": 1855,
            },
        ],
    },
]

print("------------------")
for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Idioma:", pais["idioma"])
    print("Moneda:", pais["moneda"])
    print("Ciudades:")
    for ciudad in pais["ciudades"]:
        print("☺", ciudad["nombre"])
        print("Población:", "☺", ciudad["poblacion"])
        print("Fundación:", "☺", ciudad["fundacion"])

print("------------------")
