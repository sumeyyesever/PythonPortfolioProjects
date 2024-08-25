from tkinter import *
from tkinter import messagebox
import time


class DisappearText:
    def __init__(self, root):
        self.window = root
        self.window.title("Disappearing Text Writing App")
        self.window.minsize(width=600, height=500)

        self.main_label = Label(self.window, pady=15, font=("Arial", 12, "bold"), fg="red4",
                                text="You have only 5 seconds between letters for stop and staring!")
        self.main_label.pack()

        self.text_area = Text(self.window, width=60, height=25)
        self.text_area.focus()
        self.text_area.bind("<KeyPress>", self.key_pressed)
        self.text_area.pack()

        self.last_pressed_key_time = None
        self.elapsed_time = None
        self.running = False

    def key_pressed(self, event):
        self.running = True
        time_now = time.time()
        self.last_pressed_key_time = time_now
        self.calculate_elapsed_time()

    def calculate_elapsed_time(self):
        if self.running:
            current_time = time.time()
            self.elapsed_time = current_time - self.last_pressed_key_time
            if self.elapsed_time >= 5:
                self.running = False
                self.time_out()
            else:
                window.after(1000, self.calculate_elapsed_time)

    def time_out(self):
        self.text_area.delete(1.0, END)
        self.text_area.config(state=DISABLED)
        result = messagebox.askokcancel("Oops!", "Do you want to try again?")
        if result:
            self.start_again()
        else:
            self.window.destroy()

    def start_again(self):
        self.text_area.config(state=NORMAL)
        self.text_area.delete(1.0, END)
        self.text_area.focus()

        self.last_pressed_key_time = None
        self.elapsed_time = None
        self.running = False


window = Tk()
DisappearText(window)
window.mainloop()
