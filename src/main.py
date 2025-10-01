"""Ponto de entrada principal da aplicação."""

from src.adk.agent.example_agent import run_agent


def main():
    """Função principal."""
    print("=== Bem-vindo ao Busca Vaga ===\n")
    print("Agente de busca de vagas usando Google ADK\n")
    
    # Exemplo de uso
    try:
        message = "Olá! Pode me ajudar a encontrar vagas?"
        print(f"Pergunta: {message}\n")
        
        response = run_agent(message)
        print(f"Resposta do Agente:\n{response}")
        
    except Exception as e:
        print(f"Erro ao executar agente: {e}")
        print("\nDica: Certifique-se de configurar suas credenciais do Google AI.")


if __name__ == "__main__":
    main()
