from langchain_community.tools import DuckDuckGoSearchRun

_search = DuckDuckGoSearchRun()


def buscar_na_web(query: str) -> str:
    """Busca informações atuais na web via DuckDuckGo e retorna os resultados."""
    try:
        resultado = _search.run(query)
        return resultado
    except Exception as e:
        return f"[busca indisponível: {str(e)}]"
