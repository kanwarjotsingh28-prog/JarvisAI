from backend.ai.ai_manager import AIManager
import json


class Planner:

    def __init__(self):

        self.ai = AIManager()

    def plan(self, command):

        prompt = f"""
You are a task planner.

Break the user's command into simple executable steps.

Return ONLY JSON.

Example:

User:
Open Chrome and search YouTube for Python.

Output:

[
    {{
        "intent":"OPEN_APPLICATION",
        "entity":"chrome"
    }},
    {{
        "intent":"SEARCH_YOUTUBE",
        "query":"Python"
    }}
]

User:

{command}
"""

        response = self.ai.ask(
            prompt,
            save_history=False
        )

        try:

            start = response.find("[")

            end = response.rfind("]") + 1

            return json.loads(response[start:end])

        except Exception:

            return None