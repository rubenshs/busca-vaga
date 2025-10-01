"""Agente básico para busca de vagas usando Google ADK."""

from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

SYSTEM_INSTRUCTION = """
Você é um assistente especializado em busca de vagas de emprego.

Suas responsabilidades incluem:
- Ajudar usuários a encontrar oportunidades de trabalho relevantes
- Fornecer informações sobre vagas disponíveis
- Dar dicas sobre processos seletivos
- Auxiliar na preparação para entrevistas

Seja sempre profissional, útil e empático com os candidatos.
"""

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[],
)
