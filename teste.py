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
        "revisao": {},
        "social": {},
        "tokens_usados": 0
    }

    grafo = construir_grafo()

    resultado = grafo.invoke(estado_inicial)

    print("\n📢 RESULTADO FINAL DA CAMPANHA\n")

    # pesquisa
    print("🧠 Pesquisa de mercado:\n")
    print(resultado["pesquisa"].get("conteudo", ""))

    # estratégia
    print("\n📊 Estratégia da campanha:\n")
    print(resultado["estrategia"].get("conteudo", ""))

    # copy
    print("\n✍️ Conteúdo criado:\n")
    print(resultado["copy"].get("conteudo", ""))

    # revisão criativa
    print("\n🎨 Revisão do Diretor Criativo:\n")
    print(resultado["revisao"].get("conteudo", ""))

    # social media final
    print("\n📱 Conteúdo final otimizado para redes sociais:\n")
    print(resultado["social"].get("conteudo", ""))

    print("\n💰 Tokens totais usados:", resultado["tokens_usados"])


if __name__ == "__main__":
    main()
