class PluginManager:

    def __init__(self):

        self.plugins = {}

    def register(self, intent, plugin):

        self.plugins[intent] = plugin

    def execute(self, intent, *args, **kwargs):

        plugin = self.plugins.get(intent)

        if plugin is None:
            return None

        return plugin.execute(*args, **kwargs)