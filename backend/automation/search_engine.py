import webbrowser
import urllib.parse


class SearchEngine:

    def google(self, query):

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

    def youtube(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

    def github(self, query):

        url = (
            "https://github.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)