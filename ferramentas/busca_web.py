def buscar_na_web(query: str) -> str:
    """Busca informações atuais na web via DuckDuckGo e retorna os resultados."""
    try:
        from langchain_community.tools import DuckDuckGoSearchRun
        resultado = DuckDuckGoSearchRun().run(query)
        return resultado
    except ImportError:
        return "[busca indisponível: instale duckduckgo-search]"
    except Exception as e:
        return f"[busca indisponível: {str(e)}]"
