# ========================================================
#               Author Brad Heffernan
# ========================================================
import gi
import Functions as fn
import GUI
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa


class ALN(Gtk.Window):
    def __init__(self):
        super(ALN, self).__init__(title="Arcolinux News")
        self.set_default_size(800, 600)
        self.connect('delete-event', Gtk.main_quit)

        GUI.GUI(self, Gtk, fn)


if __name__ == '__main__':
    w = ALN()
    w.show_all()
    Gtk.main()
