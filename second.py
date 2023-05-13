from tkinter import *

from tkinter.filedialog import askopenfilename, asksaveasfilename



# Create the main window

root = Tk()

root.title("Simple Text Editor")



# Create the text area

text_area = Text(root)

text_area.pack()



# Function to open a file

def open_file():

    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file_path:

        with open(file_path, "r") as file:

            content = file.read()

            text_area.delete("1.0", END)

            text_area.insert(END, content)



# Function to save the file

def save_file():

    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if file_path:

        content = text_area.get("1.0", END)

        with open(file_path, "w") as file:

            file.write(content)



# Create the menu bar

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="Save", command=save_file)

file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)



# Run the main loop

root.mainloop()
