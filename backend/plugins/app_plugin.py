from backend.automation.automation import Automation


class AppPlugin:

    def __init__(self):

        self.automation = Automation()

    def execute(self, result):

        self.automation.execute(
            result["intent"],
            result["entity"],
            result["search_engine"],
            result["search_query"]
        )

        return {
            "response": "Done."
        }