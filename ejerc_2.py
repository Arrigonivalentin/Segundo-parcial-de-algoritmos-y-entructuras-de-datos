# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia,
#     Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8

from grafo import Graph


grafo = Graph(dirigido=False)


personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]


for personaje in personajes:
    nodo = {
        'value': personaje,
        'aristas': [],
        }
    grafo.insert_vertice(personaje)



grafo.insert_arista("Luke Skywalker", "Darth Vader", "5")
grafo.insert_arista("Luke Skywalker", "Yoda", "3")
grafo.insert_arista("Darth Vader", "Yoda", "4")
grafo.insert_arista("Luke Skywalker", "Leia", "6")
grafo.insert_arista("Leia", "Han Solo", "5")
grafo.insert_arista("Yoda", "BB-8", "2")
grafo.insert_arista("Chewbacca", "Han Solo", "4")
grafo.insert_arista("Rey", "Kylo Ren", "7")
grafo.insert_arista("C-3PO", "R2-D2", "8")
grafo.insert_arista("Boba Fett", "Han Solo", "3")


grafo.show_graph()

# b) Hallar el árbol de expansión mínima y determinar si contiene a Yoda
arbol_expansion_minimo = grafo.kruskal(grafo)
print(arbol_expansion_minimo)

buscar_yoda = any("Yoda" in elementos for elementos in arbol_expansion_minimo)
if buscar_yoda is True:
    print("Yoda está presente en el árbol de expansión mínima.")
else:
    print("Yoda no está presente en el árbol de expansión mínima.")


# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
def episodios_maximos(self):
    max_weight = 0
    personajes = ("", "")

    for nodo in self.elements:
        for arista in nodo['aristas']:
            personaje1 = nodo['value']
            personaje2 = arista['value']
            peso = arista['peso']
            peso = int(peso)
            if peso > max_weight:
                max_weight = peso
                personajes = (personaje1, personaje2)

    return max_weight, personajes

print(episodios_maximos(grafo))








