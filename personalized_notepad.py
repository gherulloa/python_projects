"""Personalized Notepad
- Graphic script that uses tkinter to create a personalized notepad application.
- Application to create notes able to Create, Open and Save files."""

import os
import tkinter
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
# class to define the Notepad.
class Notepad:
    # __root is a Tkinter object.
    __root = tkinter.Tk()
    # Notepad dimensions.
    __thisWidth = 300
    __thisHeight = 300
    # Area to write the text
    __thisTextArea = tkinter.Text(__root)
    # Menu bar with its sub menus ____thisTextArea
    __thisMenuBar = tkinter.Menu(__root)
    __thisFileMenu = tkinter.Menu(__thisMenuBar, tearoff = 0)
    __thisEditMenu = tkinter.Menu(__thisMenuBar, tearoff = 0)
    __thisHelpMenu = tkinter.Menu(__thisMenuBar, tearoff = 0)
    # Add a scrollbar on the Text area.
    __thisScrollBar = tkinter.Scrollbar(__thisTextArea)
    # Empty file.
    file = None
    # Constructor to initialize the notepad object.
    def __init__(self, width, height):
        # Set icon, capture the error if the proper argument is not available.
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        # Set window size, capture the error if the proper argument is not available.
        try:
            self.__thisWidth = width
        except KeyError:
            pass
        try:
            self.__thisHeight = height
        except KeyError:
            pass
        # Set window text.
        self.__root.title("Untitled-Notepad")
        # Center the window.
        screenWidth = self.__root.winfo_screenmmwidth()
        screenHeight = self.__root.winfo_screenheight()
        # Left align and right align.
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        # Top and bottom align
        self.__root.geometry("%dx%d+%d+%d" % (self.__thisWidth, self.__thisHeight, left, top))
        # Auto resize text area.
        self.__root.grid_rowconfigure(0, weight = 1)
        self.__root.grid_columnconfigure(0, weight = 1)
        # Add controls.
        self.__thisTextArea.grid(sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)
        # Open new file.
        self.__thisFileMenu.add_command(label = "New", command = self.__newFile)
        # Open existing file.
        self.__thisFileMenu.add_command(label = "Open", command = self.__openFile)
        # Save file.
        self.__thisFileMenu.add_command(label = "Save", command = self.__saveFile)
        # Create line in the dialog.
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label = "Exit", command = self.__quitApplication)
        self.__thisMenuBar.add_cascade(label = "File", menu = self.__thisFileMenu)
        # Create cut, copy, paste options.
        self.__thisEditMenu.add_command(label = "Cut", command = self.__cut)
        self.__thisEditMenu.add_command(label = "Copy", command = self.__copy)
        self.__thisEditMenu.add_command(label = "Paste", command = self.__paste)
        # Add Edit options to the main menu.
        self.__thisMenuBar.add_cascade(label = "Edit", command = self.__thisEditMenu)
        # Create an about option and add it to the menu.
        self.__thisHelpMenu.add_command(label = "About", command = self.__showAbout)
        self.__thisMenuBar.add_cascade(label = "Help", command = self.__thisHelpMenu)
        self.__root.config(menu = self.__thisMenuBar)
        self.__thisScrollBar.pack(side = tkinter.RIGHT, fill = tkinter.Y)
        # Scrollbar adjusts automatically
        self.__thisScrollBar.config(command = self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)
        # Class methods to control the menu options.
    def __quitApplication(self): # Exit the application.
        self.__root.destroy()
    def __showAbout(self): # Show about information
        showinfo("Notepad 2.0", "Geo Hernandez")
    def __openFile(self): # Open an existing file. First option is for any file of any type.
        self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), \
                                                                                ("Text Documents", "*.txt")])
        if self.file == "": # Empty file, nothing to open.
            self.file = None
        else: # Attempt to open the file.
            self.__root.title(os.path.basename(self.file) + "-GeosNotepad") # Set window title.
            self.__thisTextArea.delete(1.0, tkinter.END) # Remove any existing text.
            file = open(self.file, "r") # Open the file.
            self.__thisTextArea.insert(1.0, file.read()) # Add the text to the notepad.
            file.close()
    def __newFile(self): # Create a new file.
        self.__root.title("Untitled-GeosNotepad")
        self.file = None
        self.__thisTextArea.delete(1.0, tkinter.END)
    def __saveFile(self): # Save the file.
        if self.file == None: # Save as new file.
            self.file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt",\
                                            filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
        elif self.file == "":
            self.file = None
        else: # Save the file.
            file = open(self.file, "w")
            file.write(self.__thisTextArea.get(1.0, tkinter.END))
            file.close()
            self.__root.title(os.path.basename(self.file) + "-Notepad")
        # Cut, copy and paste functions.
    def __cut(self):
        self.__thisTextArea.event_generate("Cut")
    def __copy(self):
        self.__thisTextArea.event_generate("Copy")
    def __paste(self):
        self.__thisTextArea.event_generate("Paste")
    # Run the app.
    def __run(self):
        self.__root.mainloop()

# Main code.
notepadApp = Notepad(width = 600, height = 400)
notepadApp._Notepad__run()