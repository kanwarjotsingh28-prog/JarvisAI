class MemoryExtractor:

    def extract(self, command):

        command = command.lower()

        if "my name is" in command:

            value = command.split("my name is")[-1].strip()

            return {
                "key": "name",
                "value": value
            }

        if "my favourite language is" in command:

            value = command.split("my favourite language is")[-1].strip()

            return {
                "key": "favorite_language",
                "value": value
            }

        return None