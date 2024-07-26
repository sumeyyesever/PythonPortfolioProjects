from tkinter import *


class TypingTest:
    def __init__(self, root):
        self.key_counter = 0
        self.window = root
        self.window.title("Typing Test")
        self.window.minsize(width=500, height=500)
        self.window.config(pady=100, padx=50)

        self.timer_text = Label(self.window, text="00:00")
        self.timer_text.pack()

        self.test_text = Text(self.window, height=5, width=50)
        self.test_text.insert("1.0", "Hello World")
        self.test_text.config(state="disabled")
        self.test_text.pack()

        self.typing_area = Text(self.window)
        self.typing_area.bind("<KeyRelease>", self.key_release)
        self.typing_area.pack()

        self.timer_button = Button(self.window, text="Start Timer")
        self.timer_button.pack()

    def key_release(self, event):
        typing_word = self.typing_area.get("1.0", END).strip()
        test_word = self.test_text.get("1.0", END).strip()

        # clear highlights
        self.test_text.tag_remove("highlight", "1.0", END)
        self.test_text.tag_remove("correct", "1.0", END)

        # add highlight
        start_index = "1.0"
        end_index = f"1.{len(typing_word)}"
        self.test_text.tag_add("highlight", start_index, end_index)
        self.test_text.tag_config("highlight", background="yellow")

        for i in range(min(len(typing_word), len(test_word))):
            if typing_word[i] != test_word[i]:
                start_index = f"1.{i}"
                end_index = f"1.{i + 1}"
                self.test_text.tag_add("highlight", start_index, end_index)
                self.test_text.tag_config("highlight", foreground="red")
            else:
                start_index = f"1.{i}"
                end_index = f"1.{i + 1}"
                self.test_text.tag_add("correct", start_index, end_index)
                self.test_text.tag_config("correct", foreground="black")


root = Tk()
TypingTest(root)
root.mainloop()
