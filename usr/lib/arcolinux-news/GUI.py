# ========================================================
#               Author Brad Heffernan
# ========================================================


def takeSecond(elem):
    return elem
import numpy as np


def GUI(self, Gtk, fn):
    items = fn.fetch_news()
    notice = fn.fetch_notice()

    self.HeaderBar = Gtk.HeaderBar()
    self.HeaderBar.set_show_close_button(True)
    self.HeaderBar.props.title = "Arcolinux News"
    self.set_titlebar(self.HeaderBar)

    sw = Gtk.ScrolledWindow()
    sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    sw.add(vbox)
    self.add(sw)

    items.sort(reverse=True)
    notice.sort(reverse=True)

    lists = np.append(notice, items)
    # print(lists)
    for file in lists:
        with open(fn.working_dir + file, "r") as f:
            lines = f.read()
            f.close()
        lb = Gtk.ListBox()
        lb.set_selection_mode(Gtk.SelectionMode.NONE)
        lbr = Gtk.ListBoxRow()
        lb.add(lbr)

        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lbl = Gtk.Label(xalign=0)
        lbl.set_line_wrap(True)
        lbl.set_markup("<span size=\"20000\"><b>" +
                       file.replace(".news", "") + "</b></span>")
        lbl2 = Gtk.Label(xalign=0)
        lbl2.set_line_wrap(True)
        lbl2.set_markup(lines)
        vbox1.pack_start(lbl, False, False, 5)
        vbox1.pack_start(lbl2, False, False, 5)
        hbox1.pack_start(vbox1, False, False, 10)
        lbr.add(hbox1)
        vbox.pack_start(lb, False, False, 10)
