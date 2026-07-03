class CommandRouter:

    def route(self, intent):

        if intent == "OPEN_APPLICATION":
            return "Automation Module"

        elif intent == "WEB_SEARCH":
            return "Automation Module"

        elif intent == "GET_WEATHER":
            return "Automation Module"

        elif intent == "SAVE_MEMORY":
            return "Memory Module"

        else:
            return "AI Module"