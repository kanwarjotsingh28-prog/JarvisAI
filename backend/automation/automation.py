from backend.automation.app_launcher import AppLauncher
from backend.automation.web_launcher import WebLauncher
from backend.automation.search_engine import SearchEngine


class Automation:

    def __init__(self):

        self.launcher = AppLauncher()
        self.web = WebLauncher()
        self.search = SearchEngine()

    def execute(
        self,
        intent,
        entity,
        search_engine=None,
        search_query=None
    ):

        if intent == "SEARCH":

            if search_engine == "google":
                self.search.google(search_query)

            elif search_engine == "youtube":
                self.search.youtube(search_query)

            elif search_engine == "github":
                self.search.github(search_query)

            print(f"Searching {search_engine}: {search_query}")

            return

        if intent != "OPEN_APPLICATION":
            return

        if entity is None:
            print("No application or website specified.")
            return

        websites = {
            "youtube",
            "chatgpt",
            "github",
            "gmail",
            "google",
            "linkedin",
            "instagram",
            "facebook",
            "twitter",
            "x"
        }

        if entity in websites:

            success = self.web.open(entity)

            if success:
                print(f"Opening {entity} website...")
            else:
                print(f"Couldn't open {entity}.")

            return

        success = self.launcher.launch(entity)

        if success:
            print(f"Opening {entity}...")
        else:
            print(f"Couldn't open {entity}.")