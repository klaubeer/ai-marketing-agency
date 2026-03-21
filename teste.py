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
        "nota_revisao": 0,
        "tentativas_revisao": 0,
        "tokens_usados": 0,
        "historico": {},
    }

    grafo = construir_grafo()

    resultado = grafo.invoke(estado_inicial)

    print("\n📢 RESULTADO FINAL DA CAMPANHA\n")

    print("🧠 Pesquisa de mercado:\n")
    print(resultado["pesquisa"].get("conteudo", ""))

    print("\n📊 Estratégia da campanha:\n")
    print(resultado["estrategia"].get("conteudo", ""))

    print("\n✍️ Conteúdo criado:\n")
    print(resultado["copy"].get("conteudo", ""))

    print("\n🎨 Revisão do Diretor Criativo:\n")
    print(resultado["revisao"].get("conteudo", ""))

    print("\n📱 Conteúdo final otimizado para redes sociais:\n")
    print(resultado["social"].get("conteudo", ""))

    print(f"\n🎯 Nota criativa final: {resultado['nota_revisao']}/10")
    print(f"🔄 Revisões realizadas: {resultado['tentativas_revisao']}")
    print(f"💰 Tokens totais usados: {resultado['tokens_usados']}")


if __name__ == "__main__":
    main()
