class CommandHandler:
    def __init__(self, handler):
        self.handler = handler

    def start(self):
        pass

    def receive_update(self, name, state):
        if name == "ALT":
            pass
        elif name == "VS":
            pass
        elif name == "HDG":
            pass
        elif name == "SPD":
            pass
        elif name == "MAN":
            pass
        elif name == "NAV":
            pass
        elif name == "APP":
            pass
        elif name == "TOGA":
            pass
        elif name == "running":
            pass

    def toggle_mode(self, name):
        self.handler.toggle_mode(name)

    def set_mode(self, name, val):
        self.handler.set_mode(name, val)
