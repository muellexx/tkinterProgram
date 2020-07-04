from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

def forward(root):
    global curr_image
    global my_label, image_list, button_back, button_forward, my_img, img_dir
    
    curr_image = curr_image + 1
    button_back['state'] = NORMAL
    if curr_image >= len(image_list) - 1:
        button_forward['state'] = DISABLED
    set_image(root)
    update_status()
    
    
def back(root):
    global curr_image
    global my_label, image_list, button_back, button_forward, my_img, img_dir
    
    curr_image = curr_image - 1
    button_forward['state'] = NORMAL
    if curr_image <= 0:
        button_back['state'] = DISABLED
    set_image(root)
    update_status()

def update_status():
    global curr_image, status, image_list
    status['text'] = "Image " + str(curr_image + 1) + " of " + str(len(image_list))

def set_image(root):
    global my_img, my_label, cuur_image
    max_size = 600, 600
    img = Image.open(os.path.join(img_dir, image_list[curr_image]))
    img.thumbnail(max_size)
    my_img = ImageTk.PhotoImage(img)
    if my_label is None:
        my_label = Label(root, image=my_img)
        my_label.grid(row=1, column=0, columnspan=3)
    else:
        my_label['image'] = my_img

def open(root):
    global my_image, img_dir, image_list, curr_image
    path = filedialog.askopenfilename(title="Select An Image", filetypes=(("png files", ["*.png", "*.jpg"]),("jpg files", "*.jpg"),("all files", "*")))
    img_dir = os.path.split(path)[0]
    image_list = [f for f in sorted(os.listdir(img_dir)) if f.endswith('.jpg') or f.endswith('.png')]
    curr_image = image_list.index(os.path.split(path)[1])
    set_image(root)
    update_status()
    button_forward['state'] = NORMAL
    button_back['state'] = NORMAL
    if curr_image == 0:
        button_back['state'] = DISABLED
    if curr_image >= len(image_list) - 1:
        button_forward['state'] = DISABLED

def add_imageviewer(root):
    global curr_image, status, image_list, button_back, button_forward, my_label, my_img, img_dir
    
    max_size = 300, 300

    open_image = Button(root, text="Open File", command=lambda: open(root))
    open_image.grid(row=0, column=1, pady=5)

    img_dir = ''

    curr_image = 0

    image_list = []

    my_label = None
    
    status = Label(root, text="Open an Image", bd=1, relief=SUNKEN, anchor=E)

    button_back = Button(root, state=DISABLED, text="<<", command=lambda: back(root))
    button_forward = Button(root, state=DISABLED, text=">>", command=lambda: forward(root))
    button_exit = Button(root, text="Exit Program", command=root.quit)

    button_back.grid(row=2, column=0)
    button_exit.grid(row=2, column=1, pady=10)
    button_forward.grid(row=2, column=2)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)
