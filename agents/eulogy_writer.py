from utils.claude_client import ask_claude

def write_eulogy(decision, analysis):
    with open("prompts/eulogy_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

        full_prompt = f"""
        {system_prompt}
        
        Decision: {decision}
        Analysis: {analysis}
        """

        response = ask_claude(full_prompt)
        return response