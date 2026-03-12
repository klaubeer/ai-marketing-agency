from dotenv import load_dotenv
load_dotenv()

from orquestrador.grafo_agentes import construir_grafo


def main():

    print("\n🚀 Sistema de Agência de Marketing IA\n")

    produto = input("Digite o produto da campanha: ")

    estado_inicial = {
        "produto": produto,
        "pesquisa": {},
        "estrategia": {},
        "copy": {},
        "social": {},
        "tokens_usados": 0
    }

    grafo = construir_grafo()

    resultado = grafo.invoke(estado_inicial)

    print("\n📢 CAMPANHA FINAL\n")

    print(resultado["social"]["conteudo"])

    print("\n💰 Tokens totais usados:", resultado["tokens_usados"])


if __name__ == "__main__":
    main()
