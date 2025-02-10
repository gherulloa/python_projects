"""Text Reverser GUI
- The application reverses text entered in a text field.
- The window contains a blank text field, a reverse button and a quit button.
- After text is typed in the field, click the reverse button and a new window pops up with the reversed version."""

import tkinter as tk

class ReverseTextGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Reverse Text")
        self.master.geometry("500x200")
        self.instruction_label = tk.Label(self.master, text = "Type some text and I'll reverse it.")
        self.instruction_label.pack(pady = 10)

        self.text_field = tk.Entry(self.master)
        self.text_field.pack(pady = 5)

        self.reverse_button = tk.Button(self.master, text = "Reverse", command = self.reverse_text)
        self.reverse_button.pack(pady = 5)

        self.quit_button = tk.Button(self.master, text = "Quit", command = self.master.destroy)
        self.quit_button.pack(side = "bottom", padx = 10, pady = 10)
    
    def reverse_text(self):
        text = self.text_field.get()
        rvrs_text = text[::-1]
        self.show_text("Reversed text:", rvrs_text)
    
    def show_text(self, title, message):
        msg_window = tk.Toplevel(self.master)
        msg_window.title(title)
        msg_window.geometry("300x150")

        msg_label = tk.Label(msg_window, text = message)
        msg_label.pack(pady = 20)

        ok_bttn = tk.Button(msg_window, text = "Ok", command = msg_window.destroy)
        ok_bttn.pack()

main = tk.Tk()
app = ReverseTextGUI(main)
main.mainloop()