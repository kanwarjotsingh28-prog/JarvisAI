from backend.automation.app_launcher import AppLauncher


class Automation:

    def __init__(self):

        self.launcher = AppLauncher()

    def execute(self, intent, entity):

        if intent == "OPEN_APPLICATION":

            if entity is None:

                print("No application specified.")

                return

            success = self.launcher.launch(entity)

            if success:

                print(f"Opening {entity}...")

            else:

                print(f"Couldn't open {entity}.")