import json

from backend.ai.ai_manager import AIManager


class MemoryExtractor:

    def __init__(self):

        self.ai = AIManager()

    def extract(self, command):

        prompt = f"""
You are JARVIS's memory extraction system.

Your job is to extract ONE memory from the user's sentence.

Return ONLY valid JSON.

Examples

User:
Remember that my name is Kanwarjot.

Output:
{{
    "key": "name",
    "value": "Kanwarjot"
}}

User:
Remember that I was born in Amritsar.

Output:
{{
    "key": "birth_city",
    "value": "Amritsar"
}}

User:
Remember that my laptop has an Intel Core i3 5th Gen processor.

Output:
{{
    "key": "laptop_cpu",
    "value": "Intel Core i3 5th Gen processor"
}}

Sentence:

{command}
"""

        response = self.ai.ask(
            prompt,
            save_history=False
        )

        try:

            start = response.find("{")
            end = response.rfind("}") + 1

            return json.loads(response[start:end])

        except Exception:

            return None

    def extract_recall_key(self, command):

        prompt = f"""
You are JARVIS.

The user wants to recall a memory.

Return ONLY JSON.

Example

User:
What's my name?

Output:
{{
    "key":"name"
}}

User:
Where was I born?

Output:
{{
    "key":"birth_city"
}}

User:
What processor does my laptop have?

Output:
{{
    "key":"laptop_cpu"
}}

Sentence:

{command}
"""

        response = self.ai.ask(
            prompt,
            save_history=False
        )

        try:

            start = response.find("{")
            end = response.rfind("}") + 1

            return json.loads(response[start:end])

        except Exception:

            return None