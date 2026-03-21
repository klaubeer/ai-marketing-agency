from typing import TypedDict, Dict, Any, Optional


class EstadoCampanha(TypedDict):

    # input inicial
    produto: str

    # outputs dos agentes
    pesquisa: Dict[str, Any]
    estrategia: Dict[str, Any]
    copy: Dict[str, Any]
    social: Dict[str, Any]

    # revisão criativa
    revisao: Optional[Dict[str, Any]]

    # loop de revisão
    nota_revisao: int        # nota dada pelo diretor criativo (0–10)
    tentativas_revisao: int  # quantas vezes o loop copywriter → diretor rodou

    # métricas
    tokens_usados: int

    # debug / observabilidade
    historico: Optional[Dict[str, Any]]
