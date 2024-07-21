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



    font_label = Label(property_window, text="Font")
    font_label.grid(row=1, column=0)

    choose_font = ttk.Combobox(property_window)
    choose_font["values"] = ("Arial", "Courier", "Times", "Helvetica")
    choose_font.current(0)
    choose_font.grid(row=1, column=1)

    color_label = Label(property_window, text="Color")
    color_label.grid(row=2, column=0)

    choose_color = ttk.Combobox(property_window)
    choose_color["values"] = ("Black", "Red", "Blue", "Green", "Purple")
    choose_color.current(0)
    choose_color.grid(row=2, column=1)

    font_size_label = Label(property_window, text="Size")
    font_size_label.grid(row=3, column=0)

    scale_var = IntVar()

    scale_font = Scale(property_window, from_=5, to=30, orient=HORIZONTAL, variable=scale_var)
    scale_font.grid(row=3, column=1)

    main_label = Label(text="")




    def show_changes():
        font_dict = {
            'Arial': font.Font(family='Arial', size=scale_var.get()),
            'Courier': font.Font(family='Courier', size=scale_var.get()),
            'Times': font.Font(family='Times', size=scale_var.get()),
            'Helvetica': font.Font(family='Helvetica', size=scale_var.get(), weight='bold'),
        }

        window_label = canvas.create_window(160, 280, window=main_label)
        combo_font = choose_font.get()
        font_name = font_dict[combo_font]
        main_label.config(text=entry.get(), font=font_name, fg=choose_color.get())

        def delete_changes():
            canvas.delete(window_label)

        def close_property():
            canvas.delete(window_label)
            property_window.destroy()


        delete_button = Button(property_window, text="Delete the Changes", command=delete_changes)
        delete_button.grid(row=5, column=0)

        property_window.protocol("WM_DELETE_WINDOW", close_property)






    show_button = Button(property_window, text="Show the Changes", command=show_changes)
    show_button.grid(row=4, column=0)

    save_button = Button(property_window, text="Save the Changes")
    save_button.grid(row=4, column=1)








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
