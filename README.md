# ai-quickprojects

```markdown
<div align="center">

# 🤖 ai-quickprojects

### 20 dias. 20 projetos. Da API ao deploy em produção.

*Um desafio pessoal para construir competências reais em AI Engineering,*
*um projeto prático de cada vez.*

[![Status](https://img.shields.io/badge/Desafio-✅%20Completo-brightgreen?style=for-the-badge)](https://github.com/gustavomauler/ai-quickprojects)
[![Dias](https://img.shields.io/badge/Dias-20%2F20-blue?style=for-the-badge)](https://github.com/gustavomauler/ai-quickprojects)
[![Projetos](https://img.shields.io/badge/Projetos-20%20Completos-purple?style=for-the-badge)](https://github.com/gustavomauler/ai-quickprojects)
[![Feito em](https://img.shields.io/badge/Feito%20em-Portugal%20🇵🇹-red?style=for-the-badge)](https://github.com/gustavomauler/ai-quickprojects)

</div>

---

## 📖 Sobre este repositório

Este repositório documenta um desafio de **20 dias consecutivos** onde construí um projeto prático de AI por dia — partindo do zero absoluto (um simples "Hello World" com a API do Claude) até sistemas completos com **agentes autónomos, RAG, CI/CD, deploys em produção e automações visuais**.

O objetivo não foi aprender a teoria. Foi **construir coisas que funcionam**, perceber o que falha, e desenvolver a intuição de um AI Engineer.

> *"A melhor forma de aprender AI Engineering é construir, quebrar e voltar a construir."*

---

## 🏆 Progresso do Desafio

```
Semana 1 — Fundações   ████████████████████ 100%  ✅
Semana 2 — APIs & Deploy ████████████████████ 100%  ✅
Semana 3 — Agentes      ████████████████████ 100%  ✅
Semana 4 — Produção     ████████████████████ 100%  ✅
```

---

## 📋 Todos os Projetos

| Dia | Projeto | Tecnologias | Highlights |
|-----|---------|-------------|------------|
| 🟢 **01** | [Setup & Estrutura do Repositório](./day-01/) | Git, GitHub | Estrutura modular que escalou pelos 20 dias |
| 🟢 **02** | [Hello World com Claude API](./day-02/) | Python, Anthropic SDK | Primeira chamada real à API, gestão de API keys |
| 🟢 **03** | [Resumidor de Texto CLI](./day-03/) | Python, argparse | Prompts parametrizados via linha de comandos |
| 🟢 **04** | [GitHub Actions + Lint Automático](./day-04/) | GitHub Actions, ruff | Pipeline CI funcional a partir do dia 4 |
| 🟢 **05** | [Chatbot com Histórico de Conversa](./day-05/) | Python, Anthropic SDK | Gestão de contexto e histórico de mensagens |
| 🟢 **06** | [Analisador de Emails com JSON](./day-06/) | Python, Anthropic SDK | Structured outputs, classificação automática |
| 🟢 **07** | [Webhook com FastAPI](./day-07/) | FastAPI, Python | API REST com endpoint `/process` funcional |
| 🟢 **08** | [Deploy Automático no Railway](./day-08/) | Railway, GitHub Actions | CI/CD completo, deploy a cada push |
| 🟢 **09** | [Gerador de CHANGELOG Automático](./day-09/) | Python, Git, Anthropic SDK | AI a analisar git log e gerar changelogs |
| 🟢 **10** | [Automação Visual com n8n](./day-10/) | n8n, FastAPI | Low-code + API, workflows visuais |
| 🟢 **11** | [Agente com Tool Use (Weather API)](./day-11/) | Anthropic SDK, APIs externas | Tool use real, agente que chama APIs |
| 🟢 **12** | [Agente de Gestão de Ficheiros](./day-12/) | Python, Anthropic SDK | Agente com ferramentas de read/write/list |
| 🟢 **13** | [RAG para Perguntas sobre PDFs](./day-13/) | PyMuPDF, Python, Anthropic SDK | Retrieval-Augmented Generation do zero |
| 🟢 **14** | [CI/CD com pytest + Análise por IA](./day-14/) | GitHub Actions, pytest, Anthropic SDK | AI a analisar erros de testes automaticamente |
| 🟢 **15** | [Agente de Research com Web Search](./day-15/) | Anthropic SDK, Web Search | Agente que pesquisa, cita fontes e resume |
| 🟢 **16** | [Interface Web de Chat](./day-16/) | FastAPI, HTML, JavaScript | Front-end funcional em HTML/JS puro |
| 🟢 **17** | [Especialista de Code Review](./day-17/) | Python, Anthropic SDK | System prompts avançados, personas especializadas |
| 🟢 **18** | [Pipeline de Categorização de CSVs](./day-18/) | pandas, Python, Anthropic SDK | AI + dados estruturados, batch processing |
| 🟢 **19** | [Documentação Automática de Funções](./day-19/) | Python, Anthropic SDK, AST | Análise de código e geração de docstrings |
| 🟢 **20** | [README de Portfólio Gerado com IA](./day-20/) | Python, Anthropic SDK | AI a escrever sobre os próprios projetos |

---

## 🧠 O Que Aprendi

Vinte dias de projetos diários ensinam coisas que nenhum tutorial consegue — principalmente porque nada corre sempre como previsto.

### 🔑 Insights principais

**Sobre AI Engineering**
- **Prompts são código.** Um prompt mal estruturado é tão problemático quanto uma função mal escrita. A diferença entre um output inútil e um output excelente é muitas vezes apenas a forma como a instrução é formulada.
- **Tool use muda tudo.** Quando um agente pode chamar APIs reais e interagir com sistemas externos (Dia 11, 12), deixa de ser um gerador de texto e passa a ser um actor no mundo real. Isso é simultaneamente impressionante e requer cuidado adicional.
- **RAG não é magia, é engenharia.** Implementar RAG do zero (Dia 13) desmistificou completamente a tecnologia — é chunking, embeddings e retrieval bem feitos. A complexidade real está nos detalhes.
- **Structured outputs são subestimados.** Pedir JSON estruturado ao modelo (Dia 6, 18) transforma AI numa peça integrável em qualquer pipeline de dados real.

**Sobre desenvolvimento e deploy**
- **CI/CD desde o dia 1 muda a mentalidade.** Ter GitHub Actions desde o Dia 4 fez com que cada commit fosse feito com mais cuidado e cada projeto ficasse mais limpo.
- **FastAPI é o parceiro perfeito para AI.** A velocidade de desenvolvimento é impressionante para construir APIs que expõem capacidades de AI.
- **Deploy não é o fim — é o início.** Ver um projeto a correr em produção no Railway (Dia 8) mostrou que a distância entre "funciona no meu computador" e "funciona para toda a gente" é onde mora a aprendizagem real.

**Sobre o processo**
- **Um projeto por dia força foco.** Sem a pressão de entregar algo funcional todos os dias, é fácil ficar preso na perfeição. A restrição de tempo é uma feature, não um bug.
- **Os projetos mais simples ensinam mais.** O Dia 2 (Hello World) estabeleceu padrões de gestão de API keys e estrutura de código que se mantiveram relevantes até ao Dia 20.

---

## 🛠️ Stack Tecnológico

<div align="center">

![Python](https://img.shields.io/badge/Python_3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic_Claude-D4A843?style=for-the-badge&logo=anthropic&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-CC0000?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)

</div>

| Categoria | Tecnologias |
|-----------|-------------|
| **Linguagem** | Python 3.14 |
| **AI / LLM** | Anthropic API (Claude 3.5 Sonnet) |
| **Web Framework** | FastAPI + Uvicorn |
| **CI/CD** | GitHub Actions, Railway |
| **Automação** | n8n |
| **Dados** | pandas, PyMuPDF |
| **Qualidade de Código** | ruff, pytest |
| **Outros** | argparse, Git hooks, HTML/JS vanilla |

---

## 🚀 Como Correr Localmente

### Pré-requisitos

- Python 3.11+
- Uma [API key da Anthropic](https://console.anthropic.com/)
- `git` instalado

### Setup inicial

```bash
# 1. Clonar o repositório
git clone https://github.com/gustavomauler/ai-quickprojects.git
cd ai-quickprojects

# 2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instalar dependências base
pip install anthropic python-dotenv

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env e adicionar a tua ANTHROPIC_API_KEY
```

### Correr um projeto específico

Cada dia tem o seu próprio directório e README com instruções específicas:

```bash
# Exemplo: Dia 5 — Chatbot com histórico
cd day-05
pip install -r requirements.txt  # se existir
python chatbot.py

# Exemplo: Dia 7 — API FastAPI
cd day-07
pip install fastapi uvicorn
uvicorn main:app --reload
# → Abrir http://localhost:8000/docs
```

### Variáveis de ambiente necessárias

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...       # Obrigatório para todos os projetos
WEATHER_API_KEY=...                 # Dia 11 — Weather Agent
```

---

## 📁 Estrutura do Repositório

```
ai-quickprojects/
├── .github/
│   └── workflows/          # GitHub Actions (lint, testes, deploy)
├── day-01/                 # Setup & estrutura
├── day-02/                 # Hello World Claude API
├── day-03/                 # Resumidor CLI
│   ├── summarizer.py
│   └── README.md
├── ...
├── day-20/                 # README gerado por IA
├── .env.example            # Template de variáveis de ambiente
├── .gitignore
└── README.md               # Este ficheiro
```

> Cada directório `day-XX/` contém o código do projeto, um `README.md` individual com contexto e aprendizagens, e (quando aplicável) `requirements.txt` próprio.

---

## 📊 Métricas do Desafio

```
📅 Duração total      → 20 dias consecutivos
🐍 Linhas de Python   → ~2,400 linhas
⚙️  Workflows CI/CD   → 4 pipelines configurados
🚀 Deploys produção   → 1 app live no Railway
🤖 Chamadas à API     → Centenas de requests reais
📄 Ficheiros criados  → 60+ ficheiros de código
☕ Cafés consumidos   → Não contados (mas muitos)
```

---

## 🗺️ O Que Vem a Seguir

Este desafio foi o início, não o fim. Os próximos passos naturais:

- [ ] **Multi-agent systems** — agentes que colaboram entre si
- [ ] **Fine-tuning** — modelos especializados para domínios específicos
- [ ] **LangChain / LlamaIndex** — explorar frameworks de alto nível
- [ ] **Vector databases** — Pinecone, Weaviate para RAG em escala
- [ ] **Streaming responses** — UX mais fluida nas interfaces de chat
- [ ] **Observabilidade** — logging e monitoring de LLM em produção

---

## 👤 Autor

<div align="center">

**Gustavo Mauler**
*AI Engineer em construção · Portugal 🇵🇹*

[![GitHub](https://img.shields.io/badge/GitHub-gustavomauler-181717?style=for-the-badge&logo=github)](https://github.com/gustavomauler)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gustavo_Mauler-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/gustavomauler)

</div>

Sou um developer português apaixonado por AI e automação. Este desafio de 20 dias foi a forma que encontrei de sair da teoria e mergulhar na construção de sistemas de AI reais — de scripts simples a agentes autónomos com ferramentas e deploys em produção.

Se tens perguntas sobre algum projeto, ideias para colaborar, ou queres apenas trocar experiências sobre AI Engineering, não hesites em contactar.

---

## 📄 Licença

Este projeto está sob a licença MIT. Podes usar, modificar e distribuir livremente — com atribuição.

```
MIT License — Gustavo Mauler, 2025
```

---

<div align="center">

*Construído com ☕, 🐍 e muita curiosidade em Portugal 🇵🇹*

**Se este repositório foi útil, deixa uma ⭐ — significa muito!**

</div>
```

---

## 💡 Notas sobre este README

Alguns detalhes de implementação para ficares com um README perfeito:

**Antes de publicar, lembra-te de:**

1. **Criar o `.env.example`** com todas as keys necessárias (sem valores reais)
2. **Verificar os links** — cada `./day-XX/`