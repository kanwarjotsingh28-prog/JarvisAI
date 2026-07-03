class SearchParser:

    def parse(self, command: str):

        # Convert everything to lowercase
        command = command.lower()

        # Default search engine
        engine = "google"

        # Detect search engine
        if "youtube" in command:
            engine = "youtube"

        elif "github" in command:
            engine = "github"

        # Remove unnecessary words
        query = command

        words_to_remove = [
            "search",
            "for",
            "google",
            "youtube",
            "github"
        ]

        for word in words_to_remove:
            query = query.replace(word, "")

        # Remove extra spaces
        query = query.strip()

        # Return both values
        return engine, query