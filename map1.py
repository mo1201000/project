
from tkinter import *
import tkintermapview

root = Tk()
root.title(' Map view')

root.geometry('1000x800')
my_label=LabelFrame(root)
my_label.pack(pady=20)

map_widget=tkintermapview.TkinterMapView(my_label, width=900 ,height=700)
#set coordinates
map_widget.set_position(31.417539,31.814443)
#set address
map_widget.set_address('horus university, New Damietta City, Egypt')
#set zoom
map_widget.set_zoom(18)

map_widget.pack()

root.mainloop()