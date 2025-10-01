# Arquitetura do Sistema Busca Vaga

## Visão Geral

O **Busca Vaga** é um sistema de agentes inteligentes para busca de vagas de emprego, construído com o **Google ADK (Agent Development Kit)**. A arquitetura segue uma abordagem modular e em camadas, utilizando o modelo **Gemini 2.0 Flash** para processamento de linguagem natural.

## Estrutura de Diretórios

```
src/
├── adk/                    # Módulo principal de agentes ADK
│   ├── agent/              # Implementações de agentes
│   │   ├── example_agent.py
│   │   └── __init__.py
│   ├── tools/              # Ferramentas para os agentes
│   │   └── __init__.py
│   └── __init__.py
├── adapters/               # Camada de adaptadores
│   └── __init__.py
├── repositories/           # Camada de acesso a dados
│   └── __init__.py
├── main.py                 # Ponto de entrada da aplicação
├── root_agent.yaml         # Configuração do agente raiz
└── __init__.py
```

## Camadas da Arquitetura

### 1. **Camada de Agentes (ADK)**
- **Localização**: `src/adk/agent/`
- **Responsabilidade**: Implementação dos agentes inteligentes usando Google ADK
- **Componentes atuais**:
  - `example_agent.py`: Agente básico configurado com instruções específicas para busca de vagas
  - Modelo: `gemini-2.0-flash`
  - Sistema de instruções define comportamento como assistente especializado

**Características do Agente Atual**:
- Nome: `weather_time_agent` (nome genérico, mas instruções voltadas para vagas)
- Instruções do sistema focadas em:
  - Busca de oportunidades de trabalho
  - Informações sobre vagas
  - Dicas de processos seletivos
  - Preparação para entrevistas

### 2. **Camada de Ferramentas (Tools)**
- **Localização**: `src/adk/tools/`
- **Responsabilidade**: Ferramentas e funções que os agentes podem utilizar
- **Estado atual**: Estrutura criada, aguardando implementação de ferramentas específicas

**Ferramentas potenciais**:
- Busca em APIs de vagas
- Scraping de sites de emprego
- Filtros e processamento de dados
- Integração com plataformas de recrutamento

### 3. **Camada de Adaptadores**
- **Localização**: `src/adapters/`
- **Responsabilidade**: Interface entre o sistema e serviços externos
- **Padrão**: Adapter Pattern para desacoplar integrações
- **Estado atual**: Estrutura preparada para implementações futuras

**Adaptadores esperados**:
- APIs de sites de vagas (LinkedIn, Indeed, etc.)
- Serviços de notificação
- Sistemas de autenticação
- Integrações com calendários/agendas

### 4. **Camada de Repositórios**
- **Localização**: `src/repositories/`
- **Responsabilidade**: Acesso e persistência de dados
- **Padrão**: Repository Pattern para abstração de dados
- **Estado atual**: Estrutura pronta para implementação

**Repositórios potenciais**:
- Repositório de vagas
- Repositório de usuários/candidatos
- Repositório de histórico de buscas
- Cache de resultados

### 5. **Configuração de Agentes**
- **Arquivo**: `src/root_agent.yaml`
- **Formato**: YAML com schema do ADK
- **Conteúdo atual**:
  - Classe: `LlmAgent`
  - Modelo: `gemini-2.5-flash`
  - Delegação para agentes especializados (weather_agent mencionado)

## Padrões Arquiteturais

### Clean Architecture
A estrutura segue princípios de **Clean Architecture**:
- Separação clara de responsabilidades
- Independência de frameworks
- Testabilidade facilitada
- Inversão de dependências

### Camadas de Separação
```
┌──────────────────────────────────┐
│      Camada de Agentes (ADK)     │  ← Lógica de IA e processamento
├──────────────────────────────────┤
│     Camada de Ferramentas        │  ← Funções executáveis pelos agentes
├──────────────────────────────────┤
│     Camada de Adaptadores        │  ← Interface com sistemas externos
├──────────────────────────────────┤
│     Camada de Repositórios       │  ← Acesso e persistência de dados
└──────────────────────────────────┘
```

## Fluxo de Execução

### Fluxo Principal
1. **Entrada**: Usuário executa `uv run busca-vaga` ou importa o módulo
2. **Main**: `src/main.py` carrega variáveis de ambiente (.env)
3. **Agente**: Sistema instancia o agente configurado
4. **Processamento**: Agente processa requisições usando Gemini
5. **Ferramentas**: Agente pode chamar ferramentas conforme necessário
6. **Adaptadores**: Ferramentas usam adaptadores para acessar APIs externas
7. **Repositórios**: Dados são persistidos ou recuperados via repositórios
8. **Resposta**: Resultado é retornado ao usuário

### Configuração de Ambiente
- Arquivo `.env` para variáveis sensíveis
- `GOOGLE_API_KEY` necessária para funcionamento
- `dotenv` carrega configurações automaticamente

## Tecnologias e Dependências

### Core
- **Python**: >= 3.12
- **Google ADK**: >= 1.15.1
- **python-dotenv**: Gerenciamento de variáveis de ambiente
- **Gemini 2.0 Flash**: Modelo de IA para agentes

### Gerenciamento
- **uv**: Gerenciador de pacotes e ambiente virtual