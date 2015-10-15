import subprocess
import inspect
import os
import gtk
from gi.repository import GObject, Gedit, Gtk


class WcPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "WcPlugin"
    window = GObject.property(type=Gedit.Window)
    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        #print("Window %s activated." % self.window)

        # Find the status bar, add a new label to show the branch
        status_bar = self.window.get_statusbar()
        self.label = Gtk.Label(None)
        self.label.set_selectable(False)
        self.label.set_single_line_mode(True)
        self.label.show()

        # Add a container, so the Label does not overflow the vspace of the statusbar
        self.container = Gtk.Frame()
        self.container.show()
        self.container.add(self.label)
        status_bar.pack_end(self.container, expand=False, fill=True, padding=2)

        # show all
        self.do_update_state()

    def do_deactivate(self):
        #print("Window %s deactivated." % self.window)
        pass

    def do_update_state(self):
        #print("Window %s state updated." % self.window)
        label_text = u'wc Plugin: save file for info'
        try:
            doc = self.window.get_active_document()
            if doc is not None:
                location = doc.get_location()
                if location is not None:
                    filename = location.get_basename()
                    path = os.path.dirname(location.get_path())
                    full_filename = os.path.join(path, filename)
                    #print("Filename %s " % full_filename)
                    p = subprocess.Popen(["wc", full_filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    (output, err) = p.communicate()
                    #print("Output: %s" % output)
                    result = output.split()
                    lines = result[0].decode("utf-8")
                    words = result[1].decode("utf-8")
                    characters = result[2].decode("utf-8")
                    label_text = "wc Plugin: lines -> %s , words -> %s , characters -> %s " % (lines , words , characters)
        except Exception:
            raise
        except BaseException:
            raise
        finally:
            # Update the branch label
            self.label.set_markup(label_text)
