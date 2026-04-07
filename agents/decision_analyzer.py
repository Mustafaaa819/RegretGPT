from utils.claude_client import ask_claude

def analyze_decision(decision):

    with open("prompts/analyzer_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    full_prompt = f"""
    {system_prompt}
    
    Decision:
    {decision}
    """

    response = ask_claude(full_prompt)
    return response