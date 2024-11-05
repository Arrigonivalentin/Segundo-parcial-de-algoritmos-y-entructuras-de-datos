# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 

from arbol import BinaryTree
from arbol_avl import BinaryTree

tree_by_name = BinaryTree()
tree_by_number = BinaryTree()
tree_by_type = BinaryTree()


pokemons = [
    {"nombre": "bulbasaur",
     "numero": 1,
     "tipo": ["planta"]
     },
    {"nombre": "Charmander",
     "numero": 4, 
     "tipo": ["fuego"]
     },
    {"nombre": "Jolteon",
     "numero": 6,
     "tipo":  ["electrico"]
     },
     {"nombre": "Lycanroc",
      "numero": 9,
      "tipo": ["tierra"]
     },
     {"nombre": "Tyrantrum",
      "numero": 23,
      "tipo": ["acero"]
    }
]



for pokemon in pokemons:
    tree_by_name.insert_node(pokemon["nombre"], other_value=pokemon)
    tree_by_number.insert_node(pokemon["numero"], other_value=pokemon)
    for tipos in pokemon["tipo"]:
        tree_by_type.insert_node(tipos, other_value=pokemon)


def mostrar_pokemon_numero(numero):
    pokemon_by_number = tree_by_number.search(numero)
    if pokemon_by_number is not None:
        print(pokemon_by_number.other_value)
    else: print("no se encontró el pokemon con el número", numero)


# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
mostrar_pokemon_numero(4)

print()

print(tree_by_name.proximity_search("bul"))

print()

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
tree_by_type.mostrar_pokemons_por_tipo("electrico")
    
print()


# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
tree_by_number.inorden()
print ()

tree_by_name.inorden()
print()

tree_by_name.by_level()
print()

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
def mostrar_pokemon():
    for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        pokemon = tree_by_name.search(name)
        if pokemon is not None:
            print(pokemon.other_value)

mostrar_pokemon()

print()

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
def contar_tipos():
    electricos = tree_by_type.contar_pokemons_por_tipo("electrico")
    if electricos >= 1:
        print("Cantidad de Pokémon de tipo eléctrico:", electricos)
    else:
        print("no se encontraron pokemones de tipos electricos")
    print()

    aceros = tree_by_type.contar_pokemons_por_tipo("acero")
    if aceros >= 1:
        print("Cantidad de Pokemones de tipo acero:", aceros)
    else:
        print("no se encontraron pokemones de tipo acero")

contar_tipos()
















