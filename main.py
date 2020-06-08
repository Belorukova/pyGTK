import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from math import sqrt

def solve(a,b,c):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b*b - 4*a*c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Discriminant is: %.4s \n X1 is: %.4s \n X2 is: %.4s \n" % (D, x1, x2)
    elif D == 0:
        x1 = (-b + sqrt(D)) / (2*a)
        text = "Discriminant is: %.4s \n X is: %.4s \n" % (D, x1)
    else:
        text = "Discriminant is: %.4s \n No solutions" % D
    return text

def insert(value):
    """" Inserting values into text widget"""
    win.form.set_text(value)


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Quaratic equations solver")
        self.set_default_size(370, -1)
        self.set_resizable(False)

        grid = Gtk.Grid()
        self.add(grid)
        grid.set_column_spacing(5)
        grid.set_row_spacing(10)

        self.entry1 = Gtk.Entry()
        self.entry1.set_width_chars(6)
        self.label1 = Gtk.Label("x^2 +")
        self.entry2 = Gtk.Entry()
        self.entry2.set_width_chars(6)
        self.label2 = Gtk.Label("x +")
        self.entry3 = Gtk.Entry()
        self.entry3.set_width_chars(6)
        self.label3 = Gtk.Label("= 0")
        self.solve_but = Gtk.Button(label = "Solve")
        self.solve_but.connect("clicked", self.on_button_clicked)
        
        self.form = Gtk.Label()
        self.form.set_justify(Gtk.Justification.LEFT)
        
        
        grid.add(self.entry1)
        grid.attach(self.label1, 1, 0, 1, 1)
        grid.attach_next_to(self.entry2, self.label1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.label2, self.entry2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.entry3, self.label2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.label3, self.entry3, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.solve_but, self.label3, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(self.form, 0, 1, 6, 2)

    def on_button_clicked(self, button):
        """ Get the content of entries and passes result to the output area """
        try:
            a_val = float(self.entry1.get_text())
            b_val = float(self.entry2.get_text())
            c_val = float(self.entry3.get_text())
            insert(solve(a_val, b_val, c_val))
        except ValueError:
            insert("No 3 values")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
