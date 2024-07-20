from tkinter import *
from tkinter import Toplevel, font, filedialog, ttk
from PIL import Image, ImageTk


def open_image():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

    if file_path:
        img = Image.open(file_path)
        img = img.resize((300, 300))

        # convert image object to tkphoto object
        img_tk = ImageTk.PhotoImage(img)

        canvas.create_image(150,150, image=img_tk)
        canvas.image = img_tk


def open_property_window():
    property_window = Toplevel(window)
    property_window.title("Property")
    property_window.minsize(width=200, height=100)

    text_label = Label(property_window, text="Text")
    text_label.grid(row=0, column=0)

    entry = Entry(property_window, textvariable=shared_var)
    entry.focus()
    entry.grid(row=0, column=1)

    font_dict = {
        'Arial 14': font.Font(family='Arial', size=14),
        'Courier 12': font.Font(family='Courier', size=12),
        'Times 16': font.Font(family='Times', size=16),
        'Helvetica 10 bold': font.Font(family='Helvetica', size=10, weight='bold'),
     }

    font_label = Label(property_window, text="Font")
    font_label.grid(row=1, column=0)

    n = StringVar()
    choose_font = ttk.Combobox(property_window, textvariable=n)
    choose_font["values"] = ("Arial", "Courier", "Times New Roman", "Helvetica")
    choose_font.grid(row=1, column=1)
    choose_font.current(1)

    color_label = Label(property_window, text="Color")
    color_label.grid(row=2, column=0)

    choose_color = ttk.Combobox(property_window, textvariable=n)
    choose_color["values"] = ("Black", "Red", "Blue", "Green", "Purple")
    choose_color.grid(row=2, column=1)

    font_size_label = Label(property_window, text="Size")
    font_size_label.grid(row=3, column=0)

    scale_font = Scale(property_window, from_=5, to=30, orient=HORIZONTAL)
    scale_font.grid(row=3, column=1)


# creating a new window
window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=500)

shared_var = StringVar()

label_hello = Label(text="Hello")
label_hello.grid(row=0, column=1)


canvas = Canvas(window, width=350, height=350)
canvas.grid(row=1, column=2)


img_button = Button(text="Choose Image", command=open_image)
img_button.grid(row=2, column=1)

prop_button = Button(text="Add WaterMark", command=open_property_window)
prop_button.grid(row=3, column=1)

window.mainloop()
