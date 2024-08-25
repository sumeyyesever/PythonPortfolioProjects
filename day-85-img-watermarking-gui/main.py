from tkinter import *
from tkinter import Toplevel, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WaterMarkApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Image Watermarking")
        self.window.minsize(width=500, height=500)

        self.load_button = Button(self.window, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.watermark_button = Button(self.window, text="Add WaterMark", command=self.open_property_window)
        self.watermark_button.pack()

        self.save_button = Button(self.window, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.canvas = Canvas(self.window)
        self.canvas.pack()

        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((350, 350))
            self.display_image(self.image)

    def display_image(self, image):
        tk_image = ImageTk.PhotoImage(image)
        self.canvas.config(width=image.width, height=image.height)
        self.canvas.create_image(0, 0, anchor=NW, image=tk_image)
        self.canvas.image = tk_image

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"),
                                                                                         ("JPEG files", "*.jpg;*.jpeg")])
            if save_path:
                self.image.save(save_path)
                messagebox.showinfo("Info", "Image saved successfully")
        else:
            messagebox.showwarning("Warning", "No image to save.")

    def open_property_window(self):
        if self.image:
            def radio_used():
                radio_color = ()
                if radio_state.get() == 1:
                    radio_color = (255, 255, 255)
                else:
                    radio_color = (0, 0, 0)
                return radio_color

            def show_changes():
                copy_image = self.image.copy()
                width, height = copy_image.size
                draw = ImageDraw.Draw(copy_image)
                font_path = "fonts/Roboto-Bold.ttf"
                font_size = 30
                img_font = ImageFont.truetype(font_path, font_size)
                bbox = draw.textbbox((0, 0), text.get("1.0", END), font=img_font)
                text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

                x = width - text_width - 10
                y = height - text_height - 10

                text_color = radio_used()

                draw.text((x, y), text.get("1.0", END), fill=text_color, font=img_font)
                self.display_image(copy_image)

            def delete_changes():
                self.display_image(self.image)

            property_window = Toplevel(self.window)
            property_window.config(padx=20, pady=20)
            property_window.title("Property")
            property_window.minsize(width=200, height=100)

            text_label = Label(property_window, text="Watermark")
            text_label.grid(row=0, column=0, columnspan=2)

            text = Text(property_window, width=15, height=1)
            text.focus()
            text.grid(row=0, column=2, columnspan=4)

            color_label = Label(property_window, text="Color")
            color_label.grid(row=1, column=0, columnspan=2)

            radio_state = IntVar()
            radio_button_white = Radiobutton(property_window, text="White", value=1, variable=radio_state, command=radio_used)
            radio_button_black = Radiobutton(property_window, text="Black", value=2, variable=radio_state, command=radio_used)
            radio_button_white.grid(row=1, column=2, columnspan=2)
            radio_button_black.grid(row=1, column=4, columnspan=2)

            show_button = Button(property_window, text="Show Changes", command=show_changes)
            show_button.grid(row=2, column=0, columnspan=3)

            delete_button = Button(property_window, text="Delete Changes", command=delete_changes)
            delete_button.grid(row=2, column=3, columnspan=3)
        else:
            messagebox.showwarning("Warning", "Load an image first")


if __name__ == "__main__":
    window = Tk()
    app = WaterMarkApp(window)
    window.mainloop()

