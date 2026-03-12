
from typing import TypedDict, Dict, Any


class EstadoCampanha(TypedDict):
    produto: str
    pesquisa: Dict[str, Any]
    estrategia: Dict[str, Any]
    copy: Dict[str, Any]
    social: Dict[str, Any]
