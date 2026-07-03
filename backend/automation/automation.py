from backend.automation.app_launcher import AppLauncher
from backend.automation.web_launcher import WebLauncher


class Automation:

    def __init__(self):

        self.launcher = AppLauncher()
        self.web = WebLauncher()

    def execute(self, intent, entity):

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