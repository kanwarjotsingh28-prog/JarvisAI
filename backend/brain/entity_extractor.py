class EntityExtractor:

    def extract(self, command: str):

        command = command.lower()

        applications = [
            "chrome",
            "notepad",
            "calculator",
            "paint",
            "spotify",
            "vscode",
            "edge"
        ]

        for app in applications:
            if app in command:
                return app

        return None