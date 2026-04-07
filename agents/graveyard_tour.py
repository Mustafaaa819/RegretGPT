import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAVEYARD_FILE = os.path.join(BASE_DIR, "memory", "graveyard.json")


def show_cemetery():
    if not os.path.exists(GRAVEYARD_FILE) or os.path.getsize(GRAVEYARD_FILE) == 0:
        print("\n🪦 The graveyard is empty. No sins to display.")
        return

    with open(GRAVEYARD_FILE, "r", encoding="utf-8") as f:
        graveyard = json.load(f)

    print("\n--- 🕯️ TOUR OF THE CEMETERY 🕯️ ---")
    for i, grave in enumerate(graveyard, 1):
        analysis = grave['analysis']

        # 🧠 Smarter Score Detection: Checks for "Regret Score:" OR just "Score:"
        score = "N/A"
        if "Regret Score:" in analysis:
            score = analysis.split("Regret Score:")[1].split("\n")[0].strip()
        elif "Score:" in analysis:
            score = analysis.split("Score:")[1].split("\n")[0].strip()

        print(f"\n{i}. ⚰️ {grave['decision'].upper()}")
        print(f"   📅 Buried on: {grave['date']}")
        print(f"   📊 Regret Score: {score}")

    print("\n--------------------------------")

    # 🌟 NEW: Detailed View Option
    choice = input("\nEnter a Grave Number to see the full service (or Enter to go back): ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(graveyard):
            g = graveyard[idx]
            print("\n" + "=" * 50)
            print(f"🪦 GRAVE OF: {g['decision'].upper()}")
            print(f"📅 DATE: {g['date']}")
            print("-" * 20)
            print(f"\n🧠 THE AUTOPSY (Analysis):\n{g['analysis']}")
            print(f"\n{g['eulogy']}")
            print("=" * 50)
        else:
            print("That grave doesn't exist yet...")