import json
import os
from datetime import datetime

GRAVEYARD_FILE = "memory/graveyard.json"


def bury_decision(decision, analysis, eulogy):
    graveyard = []

    # 1. Check if file exists AND is not empty
    if os.path.exists(GRAVEYARD_FILE) and os.path.getsize(GRAVEYARD_FILE) > 0:
        try:
            with open(GRAVEYARD_FILE, "r", encoding="utf-8") as f:
                graveyard = json.load(f)
        except json.JSONDecodeError:
            # If the file is corrupted or weird, start fresh
            graveyard = []

    # 2. Create new grave
    new_grave = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "decision": decision,
        "analysis": analysis,
        "eulogy": eulogy
    }

    graveyard.append(new_grave)

    # 3. Save back to JSON (using utf-8 for those emojis!)
    with open(GRAVEYARD_FILE, "w", encoding="utf-8") as f:
        json.dump(graveyard, f, indent=4, ensure_ascii=False)