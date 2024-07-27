from tkinter import *
import math


class TypingTest:
    def __init__(self, root):
        self.key_counter = 0
        self.window = root
        self.window.title("Typing Test")
        self.window.minsize(width=900, height=500)
        self.window.config(pady=10, padx=20)

        self.timer_text = Label(self.window, text="00:00", height=2, width=30, bg="lightblue",
                                font=("Arial", 16, "bold"), fg="hotpink")
        self.timer_text.pack(pady=30)

        self.timer_button = Button(self.window, text="Start Timer", command=self.start_timer)
        self.timer_button.pack()

        self.test_text = Text(self.window, height=5, width=50)
        self.test_text.insert("1.0", "Hello")
        self.test_text.config(state="disabled")
        self.test_text.pack(pady=10)

        self.typing_area = Text(self.window, height=5, width=50)
        self.typing_area.bind("<KeyRelease>", self.key_release)

        self.calculate_area = Label(self.window, text="")

    def count_down(self, count):

        count_minute = math.floor(count / 60)
        count_second = count % 60
        if count_second < 10:
            count_second = f"0{count_second}"
        self.timer_text.config(text=f"{count_minute}:{count_second}")
        if count > 0:
            global timer
            timer = self.window.after(1000, self.count_down, count-1)
        else:
            self.calculate_score()

    def start_timer(self):
        self.typing_area.pack()
        self.count_down(10)

    def calculate_score(self):
        self.calculate_area.pack(pady=30)
        typing_word = self.typing_area.get("1.0", END).strip()
        test_word = self.test_text.get("1.0", END).strip()
        typing_word_array = typing_word.split(" ")
        print(typing_word_array)
        test_word_array = test_word.split(" ")
        print(test_word_array)
        correct_words = []
        wrong_words = []
        correct_characters_in_wrong = ""
        wrong_characters = ""

        for i in range(min(len(typing_word_array), len(test_word_array))):
            if typing_word_array[i] != test_word_array[i]:
                wrong_words.append(typing_word_array[i])
                for j in range(min(len(typing_word_array[i]), len(test_word_array[i]))):
                    if typing_word_array[i][j] != test_word_array[i][j]:
                        wrong_characters += typing_word_array[i][j]
                    else:
                        correct_characters_in_wrong += typing_word_array[i][j]
            else:
                correct_words.append(typing_word_array[i])

        correct_word_string = "".join(correct_words)
        print(correct_word_string)
        print(len(correct_word_string))
        print(correct_characters_in_wrong)
        total_correct = len(correct_word_string) + len(correct_characters_in_wrong)

        print(f"Your word score:{len(correct_words)}/{len(test_word_array)}")
        print(f"Your character score: {total_correct}")

        total_correct_words = len(correct_words)
        total_words = len(test_word_array)
        calculate_label_text = f"{total_correct_words} WPM {total_correct} CPM \nYour word score:{total_correct_words}/{total_words} \nYour character score: {total_correct}"

        self.calculate_area.config(text=calculate_label_text)

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
