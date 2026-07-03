import subprocess


class AppLauncher:

    def launch(self, app):

        apps = {

            "notepad": "notepad.exe",

            "calculator": "calc.exe",

            "paint": "mspaint.exe",

            "explorer": "explorer.exe",

            "cmd": "cmd.exe",

            "vscode": r"C:\Users\Administrator\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        }

        if app == "chrome":

            try:

                subprocess.Popen(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                )

                return True

            except Exception as e:

                print(f"Error: {e}")

                return False

        if app in apps:

            try:

                subprocess.Popen(apps[app])

                return True

            except Exception as e:

                print(f"Error: {e}")

                return False

        return False