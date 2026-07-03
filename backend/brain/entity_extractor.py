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

            "spotify": "spotify"
        }

        for alias, app in aliases.items():

            if alias in command:
                return app

        return None