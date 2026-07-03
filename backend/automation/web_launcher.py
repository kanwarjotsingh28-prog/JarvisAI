import webbrowser


class WebLauncher:

    def open(self, website):

        websites = {

            "youtube": "https://www.youtube.com",

            "chatgpt": "https://chat.openai.com",

            "github": "https://github.com",

            "gmail": "https://mail.google.com",

            "google": "https://www.google.com",

            "linkedin": "https://www.linkedin.com",

            "instagram": "https://www.instagram.com",

            "facebook": "https://www.facebook.com",

            "x": "https://x.com",

            "twitter": "https://x.com"

        }

        if website in websites:

            webbrowser.open(websites[website])

            return True

        return False