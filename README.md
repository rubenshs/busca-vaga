# busca-vaga

Exemplo de agentes para busca de vagas disponíveis usando Google ADK (Agent Development Kit).

## 🚀 Instalação

```bash
# Instalar dependências
uv sync

# Ou com pip
pip install -e .
```

## 🔑 Configuração

Antes de executar, configure sua chave API do Google AI:

```bash
export GOOGLE_API_KEY="sua_chave_aqui"
```

Obtenha sua chave em: https://aistudio.google.com/apikey

## 💻 Uso

### Executar o agente

```bash
uv run busca-vaga
```

### Usar no código

```python
from src.adk.agent.example_agent import run_agent

# Fazer uma pergunta ao agente
response = run_agent("Quais são as vagas em Python?")
print(response)
```

## 📁 Estrutura

```
src/
├── adk/
│   ├── agent/
│   │   └── example_agent.py  # Agente básico de busca de vagas
│   └── tools/                # Ferramentas para os agentes
├── adapters/                 # Adaptadores para integrações
├── repositories/             # Camada de dados
└── main.py                   # Ponto de entrada
```

## 🤖 Sobre o Agente

O agente utiliza o modelo **Gemini 2.0 Flash** e está configurado para:
- Ajudar na busca de vagas de emprego
- Fornecer informações sobre oportunidades
- Dar dicas sobre processos seletivos
- Auxiliar na preparação para entrevistas
