import json

x = {
    "nombre": "Ken",
    "edad": 45,
    "casados": "Cierto",
    "ninios": ("Alice", "Bob"),
    "mascotas": ["$0027Perro$0027"],
    "coches": [
            {"Modelo": "Audi A1", "mpg": 15.1},
            {"Modelo": "Zeep Compass", "mpg": 18.1}
            ]
    }
# ordenando el resultado en orden de las llaves:
sorted_string = json.dumps(x, indent=4, sort_keys=True)
print(sorted_string)

with open ("datos.json", "w") as file_write:
    json.dump(sorted_string, file_write)
    print(file_write)
    print('')