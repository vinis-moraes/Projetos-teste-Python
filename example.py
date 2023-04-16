import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)

        self.button = Gtk.Button(label="Botão do aplicativo")
        self.box1.append(self.button)
        self.button.connect('clicked', self.button_clicked)

        self.set_default_size(600,600)
        self.set_title('Example app')

        self.chck = Gtk.CheckButton(label='Check example!')
        self.box2.append(self.chck)

    def button_clicked(self, widget):
        print('Teste')
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
