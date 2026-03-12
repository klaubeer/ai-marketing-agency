from orquestrador.grafo_agentes import construir_grafo

grafo = construir_grafo()

grafo.get_graph().draw_png("grafo_agentes.png")

print("✅ Diagrama salvo como grafo_agentes.png")
