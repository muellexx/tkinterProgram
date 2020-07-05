from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

class plot_app:

    def __init__(self, root):
        self.root = root
        self.add_top_bar()
        self.add_settings_book()
        self.add_plot()
        self.add_bottom_bar()

    def add_top_bar(self):
        self.top_frame = LabelFrame(self.root)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        Button(self.top_frame, text="Button 1").grid(row=0, column=0, padx=5, pady=5)
        Button(self.top_frame, text="Button 2").grid(row=0, column=1, padx=5, pady=5)
        Button(self.top_frame, text="Button 3").grid(row=0, column=2, padx=5, pady=5)
        
        self.top_label = Label(self.top_frame, text="Buttons and Text can be added in this Frame")
        self.top_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
    def add_settings_book(self):
        self.settings_frame = LabelFrame(self.root)
        self.settings_frame.grid(row=1, column=0, rowspan=2, sticky="nsew")
        self.settings_book = ttk.Notebook(self.settings_frame)
        self.settings_book.pack(fill=BOTH, expand=1)
        self.add_settings_tab()
        self.add_plot_tab()

    def add_settings_tab(self):
        self.select_tab = ttk.Frame(self.settings_book)
        self.settings_book.add(self.select_tab, text="Settings")

        # Checkbuttons
        Checkbutton(self.select_tab, text="Toggle 1").grid(row=0, column=0, padx=5, pady=(5, 0), sticky=W)
        Checkbutton(self.select_tab, text="Toggle 2").grid(row=1, column=0, padx=5, sticky=W)
        Checkbutton(self.select_tab, text="Toggle 3").grid(row=2, column=0, padx=5, pady=(0,5), sticky=W)

        # Dropdown
        Label(self.select_tab, text="Choose the Setting").grid(row=3, column=0, padx=5, pady=(5, 0))
        options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
        clicked = StringVar()
        clicked.set(options[0]) 
        dropdown = OptionMenu(self.select_tab, clicked, *options).grid(row=4, column=0, padx=5, pady=(0,5))
        
        # Entry
        Label(self.select_tab, text="Enter the Name").grid(row=5, column=0, padx=5, pady=(5,0))
        Entry(self.select_tab).grid(row=6, column=0, padx=5, pady=(0,5), sticky="ne")

        # Radio
        Label(self.select_tab, text="Choose an Option").grid(row=7, column=0, padx=5, pady=(5,0))
        var = StringVar()
        var.set("Option 1")
        Radiobutton(self.select_tab, text="Option 1", variable=var, value="Option 1").grid(row=8, column=0, padx=5)
        Radiobutton(self.select_tab, text="Option 2", variable=var, value="Option 2").grid(row=9, column=0, padx=5)
        Radiobutton(self.select_tab, text="Option 3", variable=var, value="Option 3").grid(row=10, column=0, padx=5, pady=(0,5))

        # Slider
        Label(self.select_tab, text="Adjust the setting").grid(row=11, column=0, padx=5, pady=(5,0))
        Scale(self.select_tab, from_=0, to=200, orient=HORIZONTAL).grid(row=12, column=0, padx=5, pady=(0,5))

    def add_plot_tab(self):
        self.plot_tab = ttk.Frame(self.settings_book)
        self.settings_book.add(self.plot_tab, text="Plot")

        # Treeview
        tree=ttk.Treeview(self.plot_tab, height=25)

        tree["columns"] = ("one")
        tree.column("#0", width=100)
        tree.column("one", width=60)

        tree.heading("#0", text="Name", anchor=W)
        tree.heading("one", text="Info", anchor=W)

        folder1=tree.insert("", 1, text="Folder 1", values=("Info1"))
        tree.insert("", 2, text="File X", values=("InfoX"))
        folder2=tree.insert("", 3, text="Plots", values=("Plots"))
        folder3=tree.insert("", 3, text="Images", values=("Images"))

        tree.insert(folder1, "end", text="File A", values=("InfoA"))
        tree.insert(folder1, "end", text="File B", values=("InfoB"))
        tree.insert(folder1, "end", text="File C", values=("InfoC"))
        tree.insert(folder1, "end", text="File D", values=("InfoD"))
        tree.insert(folder1, "end", text="File E", values=("InfoE"))
        tree.insert(folder1, "end", text="File F", values=("InfoF"))
        tree.insert(folder1, "end", text="File G", values=("InfoG"))
        tree.insert(folder1, "end", text="File H", values=("InfoH"))
        tree.insert(folder1, "end", text="File I", values=("InfoI"))
        tree.insert(folder1, "end", text="File J", values=("InfoJ"))
        
        subfolder1=tree.insert(folder2, "end", text="A Plots", values=("PlotsA"))
        subfolder2=tree.insert(folder2, "end", text="B Plots", values=("PlotsB"))
        subfolder3=tree.insert(folder2, "end", text="C Plots", values=("PlotsC"))

        tree.insert(subfolder1, "end", text="Plot 1", values=("Plot1"))
        tree.insert(subfolder1, "end", text="Plot 2", values=("Plot2"))
        tree.insert(subfolder1, "end", text="Plot 3", values=("Plot3"))
        
        tree.insert(subfolder2, "end", text="Plot 1", values=("Plot1"))
        tree.insert(subfolder2, "end", text="Plot 2", values=("Plot2"))
        tree.insert(subfolder2, "end", text="Plot 3", values=("Plot3"))

        subsubfolder1=tree.insert(subfolder3, "end", text="X Plots", values=("PlotsX"))
        subsubfolder2=tree.insert(subfolder3, "end", text="Y Plots", values=("PlotsX"))
        
        tree.insert(subsubfolder1, "end", text="Plot 1", values=("Plot1"))
        tree.insert(subsubfolder1, "end", text="Plot 2", values=("Plot2"))
        tree.insert(subsubfolder1, "end", text="Plot 3", values=("Plot3"))
        
        tree.insert(subsubfolder2, "end", text="Plot 1", values=("Plot1"))
        tree.insert(subsubfolder2, "end", text="Plot 2", values=("Plot2"))
        tree.insert(subsubfolder2, "end", text="Plot 3", values=("Plot3"))
        
        sub_img1=tree.insert(folder3, "end", text="A Imgs", values=("ImgsA"))
        sub_img2=tree.insert(folder3, "end", text="B Imgs", values=("ImgsB"))
        sub_img3=tree.insert(folder3, "end", text="C Imgs", values=("ImgsC"))
        
        tree.insert(sub_img1, "end", text="Img 1", values=("Img1"))
        tree.insert(sub_img1, "end", text="Img 2", values=("Img2"))
        tree.insert(sub_img1, "end", text="Img 3", values=("Img3"))
        
        tree.insert(sub_img2, "end", text="Img 1", values=("Img1"))
        tree.insert(sub_img2, "end", text="Img 2", values=("Img2"))
        tree.insert(sub_img2, "end", text="Img 3", values=("Img3"))
        
        # Scrollbar
        vsb = ttk.Scrollbar(self.plot_tab, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")
        
        tree.grid(row=0, column=0, sticky="nsew")
        


    def add_plot(self):
        self.plot_frame = LabelFrame(self.root)
        self.plot_frame.grid(row=1, column=1)

        fig = Figure(figsize=(7,4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2*np.pi * t))

        self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    def add_bottom_bar(self):
        self.bottom_frame = LabelFrame(self.root)
        self.bottom_frame.grid(row=2, column=1, sticky="nsew")
        
        Button(self.bottom_frame, text="Button 1").grid(row=0, column=0, padx=(5,0), pady=(5,0))
        Button(self.bottom_frame, text="Button 2").grid(row=0, column=1, pady=(5,0))
        Button(self.bottom_frame, text="Button 3").grid(row=0, column=2, padx=(0,5), pady=(5,0))
        Button(self.bottom_frame, text="Button 4").grid(row=1, column=0, padx=(5,0), pady=(0,5))
        Button(self.bottom_frame, text="Button 5").grid(row=1, column=1, pady=(0,5))
        Button(self.bottom_frame, text="Button 6").grid(row=1, column=2, padx=(0,5), pady=(0,5))
        
        self.bottom_label = Label(self.bottom_frame, text="add some more controls here")
        self.bottom_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)

    
