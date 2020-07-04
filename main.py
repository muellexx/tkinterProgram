from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import menu
import calculator, imageviewer, database, weather

root = Tk()
root.title("Tkinter App")
root.iconbitmap('@/home/alex/workspace/tkinter/icon.xbm')
root.minsize(300, 300)
root.maxsize(1800,1800)

menubar = menu.add_menu(root)

tab_parent = ttk.Notebook(root)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="Calculator")
tab_parent.add(tab2, text="Image Viewer")
tab_parent.add(tab3, text="Database Example", sticky="nsew")
tab_parent.add(tab4, text="Weather")

tab_parent.pack(expand=1, fill=BOTH)

frame_calculator = Frame(tab1)
frame_imageviewer = Frame(tab2)
frame_database = Frame(tab3)
frame_weather = Frame(tab4)

# Add Apps
calculator.add_calculator(frame_calculator)
imageviewer.add_imageviewer(frame_imageviewer)

database_app = database.database_app(frame_database)
weather_app = weather.weather_app(frame_weather)

frame_calculator.pack(padx=5, pady=5)
frame_imageviewer.pack(padx=5, pady=5)
frame_database.pack(padx=5, pady=5)
frame_weather.pack(padx=5, pady=5)

root.config(menu=menubar)
root.mainloop()