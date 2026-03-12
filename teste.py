from dotenv import load_dotenv
load_dotenv()

from orquestrador.grafo_agentes import construir_grafo


def main():

    print("\n🚀 Iniciando sistema de agência de marketing com IA...\n")

    grafo = construir_grafo()

    estado_inicial = {
        "produto": "smartwatch fitness",
        "pesquisa": {},
        "estrategia": {},
        "copy": {},
        "social": {}
    }

    resultado = grafo.invoke(estado_inicial)

    print("\n📢 RESULTADO FINAL DA CAMPANHA\n")

    print("🧠 Pesquisa de mercado:\n")
    print(resultado["pesquisa"]["analise"])

    print("\n📊 Estratégia da campanha:\n")
    print(resultado["estrategia"]["plano"])

    print("\n✍️ Conteúdo da campanha:\n")
    print(resultado["copy"]["conteudo"])

    print("\n📱 Otimização para redes sociais:\n")
    print(resultado["social"]["conteudo"])


if __name__ == "__main__":
    main()
