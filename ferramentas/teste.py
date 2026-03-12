from orquestrador.grafo_agentes import construir_grafo

grafo = construir_grafo()

resultado = grafo.invoke({
    "produto": "smartwatch fitness"
})

print(resultado)
