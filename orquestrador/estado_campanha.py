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

    # métricas
    tokens_usados: int

    # debug / observabilidade
    historico: Optional[Dict[str, Any]]
