import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    window = Gtk.ApplicationWindow(application=app, title='Teste')
    window.btn = Gtk.Button(label="Cool Button!")
    window.btn.connect("clicked, ")
    window.set_child(window.btn)
    window.present()

def btn_clicked:
    print('Funcionou')

app = Gtk.Application(application_id='teste.2.vinismoraes')
app.connect('activate', on_activate)
app.run(None)