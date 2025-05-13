#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess

class XFreeRDPLauncher(Gtk.Window):
    def __init__(self):
        super().__init__(title="XFreeRDP GUI")

        self.set_border_width(10)
        self.set_default_size(300, 200)

        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        self.add(grid)

        # Pola
        self.ip_entry = Gtk.Entry()
        self.username_entry = Gtk.Entry()
        self.domain_entry = Gtk.Entry()
        self.password_entry = Gtk.Entry()
        self.password_entry.set_visibility(False)

        # Etykiety
        grid.attach(Gtk.Label(label="IP / Host:"), 0, 0, 1, 1)
        grid.attach(self.ip_entry, 1, 0, 1, 1)

        grid.attach(Gtk.Label(label="Username:"), 0, 1, 1, 1)
        grid.attach(self.username_entry, 1, 1, 1, 1)

        grid.attach(Gtk.Label(label="Password:"), 0, 2, 1, 1)
        grid.attach(self.password_entry, 1, 2, 1, 1)

        grid.attach(Gtk.Label(label="Domain:"), 0, 3, 1, 1)
        grid.attach(self.domain_entry, 1, 3, 1, 1)

        # Przycisk
        self.connect_button = Gtk.Button(label="Połącz")
        self.connect_button.connect("clicked", self.run_rdp)
        grid.attach(self.connect_button, 1, 4, 1, 1)

    def run_rdp(self, widget):
        ip = self.ip_entry.get_text()
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()
        domain = self.domain_entry.get_text()

        if not ip or not username:
            print("IP i login są wymagane.")
            return

        # Przygotuj i uruchom xfreerdp
        cmd = [
            "xfreerdp",
            f"/u:{username}",
            f"/p:{password}",
            f"/v:{ip}",
            f"/d:{domain}"
            "/cert:ignore",
            "/dynamic-resolution"
        ]
        subprocess.Popen(cmd)

win = XFreeRDPLauncher()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
