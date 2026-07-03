class EntityExtractor:

    def extract(self, command: str):

        command = command.lower()

        aliases = {

            "google chrome": "chrome",
            "chrome": "chrome",

            "visual studio code": "vscode",
            "vs code": "vscode",
            "vscode": "vscode",

            "microsoft edge": "edge",
            "edge": "edge",

            "notepad": "notepad",

            "calculator": "calculator",
            "calc": "calculator",

            "paint": "paint",

            "spotify": "spotify",

            "youtube": "youtube",

            "chatgpt": "chatgpt",

            "github": "github",

            "gmail": "gmail",

            "google": "google",

            "linkedin": "linkedin",

            "instagram": "instagram",

            "facebook": "facebook",

            "twitter": "twitter",

            "x": "x"

        }

        for alias, entity in aliases.items():

            if alias in command:

                return entity

        return None