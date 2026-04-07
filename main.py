from agents.decision_analyzer import analyze_decision
from agents.eulogy_writer import write_eulogy
from memory.graveyard_manager import bury_decision
from agents.graveyard_tour import show_cemetery
import time


def main():
    while True:
        print("\n--- ⚰️ RegretGPT: Fix Your Decisions ---")
        time.sleep(1.5)
        print("1. Bury a New Decision ⚰️")
        print("2. Visit the Cemetery 🕯️")
        print("3. Exit 👋")

        time.sleep(1)

        choice = input("\nWhat is Your Wish? ")

        if choice == "1":
            decision = input("\nTell me a decision You made: ")
            print("\n🧠 Reviewing the damage...🛠️")
            analysis = analyze_decision(decision)
            print(analysis)

            print("\n📜 Preparing the funeral service...")
            time.sleep(1)
            eulogy = write_eulogy(decision, analysis)
            print(f"\n{eulogy}")

            bury_decision(decision, analysis, eulogy)
            print("\n⚰️ Decision buried.")

        elif choice == "2":
            show_cemetery()
            input("\nPress Enter to return to the 1"
                  "1gates...")

        elif choice == "3":
            print("\nMay your decisions be less fatal. Goodbye, Human. 🚀")
            break
        else:
            print("Invalid Choice. The spirits are confused.")



if __name__ == "__main__":
    main()



