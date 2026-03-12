# ai-marketing-agency
Segue **versão em PT-BR** do README. Mantive técnico e direto para GitHub.

---

# AI Marketing Agency — Sistema Multi-Agente

Sistema multi-agente autônomo que simula uma agência de marketing para gerar campanhas completas utilizando agentes de IA.

O sistema divide uma solicitação de marketing em tarefas executadas por diferentes agentes especializados, como pesquisa de mercado, estratégia, copywriting e adaptação para redes sociais.

O projeto foi desenvolvido para demonstrar **orquestração de agentes, delegação de tarefas e workflows estruturados com LLMs**.

---

# Demo

Exemplo de entrada

```
Create a marketing campaign for a new fitness smartwatch
```

Exemplo de saída

```
Campaign Strategy
Posicionar o smartwatch como um parceiro de performance e saúde para pessoas ativas.

Target Audience
Entusiastas de fitness entre 25–40 anos que monitoram treinos e métricas de saúde.

Post Ideas
1. "Seu treinador no pulso"
2. "Acompanhe cada batimento do seu treino"
3. "Treine de forma mais inteligente"

Captions
Treine com mais inteligência. Conheça o smartwatch feito para performance.

Hashtags
#fitness #smartwatch #wearabletech #healthtech #trainingsmart

Ad Copy
Eleve seu treino com um smartwatch projetado para performance, recuperação e insights de saúde.
```

---

# Arquitetura do Sistema

O sistema simula o funcionamento de uma agência real, onde cada agente é responsável por uma etapa do processo de criação da campanha.

```
User Input
     │
     ▼
Creative Director Agent
(planejamento de tarefas)
     │
     ▼
 ┌───────────────┬───────────────┬───────────────┐
Research Agent   Strategy Agent  Copywriter Agent
        │               │               │
        └───────────────┴───────────────┘
                │
        Social Media Agent
                │
             Output
```

---

# Agentes

### Creative Director Agent

Responsável por interpretar a solicitação do usuário e delegar tarefas para os agentes apropriados.

Responsabilidades:

* decomposição de tarefas
* orquestração dos agentes
* planejamento da campanha

---

### Research Agent

Coleta insights sobre produto, mercado, concorrentes e tendências.

Saída estruturada

```
{
  "market_insights": [],
  "competitors": [],
  "trends": []
}
```

Demonstra:

* uso de ferramentas
* coleta de dados
* análise de mercado

---

### Strategy Agent

Utiliza os insights da pesquisa para definir a direção estratégica da campanha.

Saída estruturada

```
{
  "target_audience": "",
  "positioning": "",
  "campaign_angle": "",
  "channels": []
}
```

Demonstra:

* raciocínio estratégico
* planejamento de campanha

---

### Copywriter Agent

Responsável pela geração de conteúdo de marketing baseado na estratégia.

Saída estruturada

```
{
  "post_ideas": [],
  "captions": [],
  "ad_copy": ""
}
```

---

### Social Media Agent

Adapta o conteúdo da campanha para diferentes plataformas sociais.

Saída estruturada

```
{
  "instagram_posts": [],
  "tiktok_hooks": [],
  "hashtags": []
}
```

---

# Arquitetura Técnica

O sistema é implementado utilizando um workflow baseado em grafos, onde cada agente funciona como um nó que recebe e atualiza um estado compartilhado.

Fluxo simplificado

```
Research → Strategy → Copywriter → Social Media
```

Exemplo de estado compartilhado

```
CampaignState

product
research
strategy
copy
social
```

Cada agente atualiza o estado global conforme o workflow progride.

---

# Stack Tecnológica

Principais tecnologias utilizadas no projeto

* Python
* LangGraph
* LangChain
* OpenAI API
* FastAPI
* Streamlit

Função de cada componente

| Componente | Função                      |
| ---------- | --------------------------- |
| LangGraph  | Orquestração de agentes     |
| LangChain  | Abstrações para agentes LLM |
| OpenAI     | Modelo de linguagem         |
| FastAPI    | API do sistema              |
| Streamlit  | Interface para interação    |

---

# Estrutura do Projeto

```
ai-marketing-agency

agents/
   creative_director.py
   research_agent.py
   strategist_agent.py
   copywriter_agent.py
   social_media_agent.py

orchestrator/
   agent_graph.py
   state.py

tools/
   web_search.py

app/
   api.py
   ui.py

tests/
   test_agents.py

README.md
```

---

# Workflow do Sistema

```
User input
   ↓
Creative Director planeja tarefas
   ↓
Research Agent coleta insights
   ↓
Strategy Agent cria plano de campanha
   ↓
Copywriter gera conteúdo
   ↓
Social Media Agent adapta para redes sociais
   ↓
Campanha final
```

---

# O que este projeto demonstra

Este projeto demonstra diversos conceitos importantes de engenharia de IA:

* sistemas multi-agente
* orquestração de agentes
* delegação de tarefas
* saídas estruturadas de LLM
* integração com ferramentas externas
* workflows baseados em grafos
* arquitetura de sistemas de IA

---

# Possíveis melhorias

Evoluções futuras do projeto

* análise automática de concorrentes
* busca de dados de mercado em tempo real
* geração de anúncios para múltiplas plataformas
* memória entre campanhas
* agente de avaliação de campanhas

---

# Instalação

Clone o repositório

```
git clone https://github.com/yourusername/ai-marketing-agency

cd ai-marketing-agency
```

Instale as dependências

```
pip install -r requirements.txt
```

Configure as variáveis de ambiente

```
OPENAI_API_KEY=your_key
```

Executar API

```
uvicorn app.api:app --reload
```

Executar interface

```
streamlit run app/ui.py
```

3️⃣ **agent logs visuais** que fazem parecer um sistema autônomo real.

