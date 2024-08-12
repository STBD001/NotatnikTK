import tkinter as tk
from tkinter import filedialog, messagebox

#Menu
def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path=filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content=file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content=text_area.get(1.0, tk.END)
            file.write(content)

#Stowrzenie okna głównego
root=tk.Tk()
root.title("Prosty notatnik")
root.geometry("800x600")

#Pole tekstowe
text_area=tk.Text(root, wrap="word")
text_area.pack(expand='yes', fill='both')

#Paski przewijania
scroll_bar_y=tk.Scrollbar(text_area)
scroll_bar_y.pack(side=tk.RIGHT, fill=tk.Y)

scroll_bar_x=tk.Scrollbar(text_area)
scroll_bar_x.pack(side=tk.BOTTOM, fill=tk.X)

text_area.config(yscrollcommand=scroll_bar_y.set, xscrollcommand=scroll_bar_x.set)
scroll_bar_y.config(command=text_area.yview)
scroll_bar_x.config(command=text_area.xview)


#Menu
menu_bar=tk.Menu(root)
file_menu=tk.Menu(menu_bar, tearoff=0)
file_menu2=tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nowy", command=new_file)
file_menu.add_command(label="Otwórz", command=open_file)
file_menu2.add_command(label="Zapisz", command=save_file)
file_menu2.add_command(label="Zapisz jako", command=save_as_file)
file_menu.add_command(label="Wyjcie", command=root.quit)
menu_bar.add_cascade(label="Plik", menu=file_menu)
menu_bar.add_cascade(label="Zapisz", menu=file_menu2)

root.config(menu=menu_bar)

#uruchamianie
root.mainloop()