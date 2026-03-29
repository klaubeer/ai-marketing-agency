import os

from sentinela import Sentinela
from sentinela.integracoes.langchain import SentinelaCallbackHandler

_api_key = os.getenv("SENTINELA_API_KEY", "")
_url = os.getenv("SENTINELA_URL", "https://api.sentinela.klauberfischer.online")

sentinela = Sentinela(
    api_key=_api_key,
    projeto="ai-marketing-agency",
    base_url=_url,
)


def get_handler(nome: str) -> SentinelaCallbackHandler:
    return SentinelaCallbackHandler(projeto="ai-marketing-agency", nome=nome)
