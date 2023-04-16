import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

def on_activate(app):
    window = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label='Teste')
    btn.connect('clicked', lambda x:window.close())
    window.set_child(btn)
    window.present()

app = Gtk.Application(application_id='test.vinismoraes.first')
app.connect('activate', on_activate)
app.run(None)
