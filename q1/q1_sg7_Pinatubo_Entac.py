class Beaker:
    def __init__(self):
        print("Beaker appeared.")
    def __del__(self):
        print("Beaker disappeared.")


class Tray:
    def __init__(self):
        print("Tray appeared.")
    def __del__(self):
        print("Tray disappeared.")
    def hold_items(self):
        print("Tray is being used.")


class Glassware:
    def __init__(self):
        print("Glassware appeared.")
        self.beaker = Beaker()
        self.tray = Tray()

    def inspect(self):
        print("Glassware can now be used.")
        self.tray.hold_items()

    def __del__(self):
        del self.beaker
        del self.tray
        print("Glassware disappeared.")


# Execution
lab_setup = Glassware()
lab_setup.inspect()
del lab_setup