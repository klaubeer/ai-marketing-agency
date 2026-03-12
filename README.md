Live Demo  
https://agencia-mkt-ia.streamlit.app/

# AI Marketing Agency — Multi-Agent Marketing System

Sistema multi-agente que simula uma agência de marketing utilizando agentes de IA para gerar campanhas completas automaticamente.

O sistema divide uma solicitação de marketing em tarefas executadas por diferentes agentes especializados, como pesquisa de mercado, estratégia, copywriting e adaptação para redes sociais.

O projeto foi desenvolvido para demonstrar **orquestração de agentes, workflows estruturados com LLMs e pipelines de geração de conteúdo com IA.**

---

# Demo

Exemplo de entrada

```
Crie uma campanha de marketing para um teclado gamer
```

Exemplo de saída

```
Pesquisa de Mercado
Insights sobre o mercado de periféricos gamer e tendências.

Estratégia de Campanha
Público-alvo, posicionamento e abordagem da campanha.

Conteúdo de Marketing
Ideias de posts, legendas e textos de anúncio.

Conteúdo Social
Hashtags, ideias de posts e hooks para reels.
```

---

# Arquitetura do Sistema

O sistema funciona como um pipeline de agentes especializados.

Cada agente executa uma tarefa e atualiza um **estado compartilhado da campanha**.

```
User Input
     │
     ▼
Research Agent
     │
     ▼
Strategy Agent
     │
     ▼
Copywriter Agent
     │
     ▼
Creative Director Agent
     │
     ▼
Social Media Agent
     │
     ▼
Final Campaign
```

A orquestração dos agentes é feita utilizando **LangGraph**.

---

# Agentes

## Research Agent

Responsável por analisar o mercado e gerar insights sobre o produto.

Funções

* análise de mercado
* identificação de tendências
* identificação de público

Saída

```
{
 "conteudo": "análise de mercado..."
}
```

---

## Strategy Agent

Cria a estratégia de marketing baseada na pesquisa.

Funções

* definição de público-alvo
* posicionamento da campanha
* ângulo da campanha

Saída

```
{
 "conteudo": "estratégia de marketing..."
}
```

---

## Copywriter Agent

Responsável por gerar o conteúdo principal da campanha.

Funções

* ideias de posts
* legendas
* textos de anúncio

Saída

```
{
 "conteudo": "conteúdo da campanha..."
}
```

---

## Creative Director Agent

Revisa e melhora o conteúdo criado pelo copywriter.

Funções

* revisão criativa
* melhoria de linguagem
* otimização de impacto

Saída

```
{
 "conteudo": "conteúdo revisado..."
}
```

---

## Social Media Agent

Adapta o conteúdo para redes sociais.

Funções

* hashtags
* ideias de posts
* hooks para reels

Saída

```
{
 "conteudo": "conteúdo social..."
}
```

---

# Arquitetura Técnica

O sistema utiliza um workflow baseado em grafos onde cada agente é um nó.

```
Research → Strategy → Copywriter → Creative Director → Social Media
```

Todos os agentes compartilham um estado de campanha.

Exemplo de estado

```
CampaignState

produto
pesquisa
estrategia
copy
revisao
social
tokens_usados
```

Cada agente lê e atualiza esse estado.

---

# Interface Web

O sistema possui uma interface construída com **Streamlit**.

Funcionalidades

* geração de campanha a partir de um produto
* visualização das etapas da campanha
* logs de execução dos agentes em tempo real
* exportação da campanha

Exportação disponível

* JSON
* PDF
* copiar conteúdo

---

# Tech Stack

Principais tecnologias utilizadas

* Python
* LangGraph
* LangChain
* OpenAI API
* Streamlit
* ReportLab

Função de cada componente

| Componente | Função                  |
| ---------- | ----------------------- |
| LangGraph  | Orquestração de agentes |
| LangChain  | Integração com LLM      |
| OpenAI     | Modelo de linguagem     |
| Streamlit  | Interface web           |
| ReportLab  | Geração de PDF          |

---

# Estrutura do Projeto

```
ai-marketing-agency

agentes/
   agente_pesquisa.py
   agente_estrategia.py
   agente_copywriter.py
   diretor_criativo.py
   agente_social_media.py

orquestrador/
   grafo_agentes.py
   estado_campanha.py
   config_llm.py

app/
   app.py

outputs/

teste.py
requirements.txt
README.md
```

---

# Execução

Clone o repositório

```
git clone https://github.com/yourusername/ai-marketing-agency

cd ai-marketing-agency
```

Instale dependências

```
pip install -r requirements.txt
```

Configure variável de ambiente

```
OPENAI_API_KEY=your_key
```

Execute a interface

```
streamlit run app/app.py
```

Acesse

```
http://localhost:8501
```

---

# O que este projeto demonstra

Este projeto demonstra conceitos importantes de engenharia de IA:

* sistemas multi-agente
* orquestração de agentes
* workflows com LLM
* pipelines de geração de conteúdo
* estado compartilhado entre agentes
* interfaces de demonstração para sistemas de IA

---

# Possíveis melhorias

Evoluções futuras

* busca de mercado em tempo real
* análise automática de concorrentes
* memória entre campanhas
* avaliação automática de campanhas
* integração com APIs de marketing
