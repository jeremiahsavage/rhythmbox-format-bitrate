from gi.repository import GObject, RB, Peas

class FormatBitratePlugin (GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super(FormatBitratePlugin, self).__init__()

    def do_activate(self):
        print("Hello World")

    def do_deactivate(self):
        del self.string
