import customtkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import utils
from PIL import Image
import os

customtkinter.set_appearance_mode("Sytem")
customtkinter.set_default_color_theme("green")

current_path = os.path.dirname(os.path.realpath(__file__))

models = f"{current_path}/models/u2net.quant.onnx"
rmbg = utils.BackgroundRemover(models)

file = ""
output_file = ""

folder_path = f"{current_path}/outputs"
if os.path.exists(folder_path):
    print(f"The {folder_path} folder already exists.")
else:
    os.makedirs(folder_path)
    print(f"The {folder_path} folder has been created.")

def open_file():
    global file
    f_types = [('Jpg Files', '*.jpg'),
                ('PNG Files','*.png'),
                ('Jpeg Files','*.jpeg')]
    file = filedialog.askopenfilename(filetypes=f_types)      

def process():
    global file
    global output_file

    if path.get() != "":
        file = path.get()

    no_bg = rmbg.remove(file)
    path_out = file.split("/")[-1].split(".")[0]
    output_file = f"{current_path}/outputs/{path_out}.png"
    no_bg.save(output_file)
    print("-- Done --")

    raw_og = Image.open(file)
    raw_bg = Image.open(output_file)
    
    image_og = customtkinter.CTkImage(raw_og, size=(600, 600))
    image_bg = customtkinter.CTkImage(raw_bg, size=(600, 600))
    
    tab_bg = customtkinter.CTkLabel(master=bg_tab, text="", image=image_bg, anchor="center")
    tab_bg.grid(row=0, column=0, padx=20, pady=5, sticky="ew")

    tab_og = customtkinter.CTkLabel(master=og_tab, text="", image=image_og, anchor="center")
    tab_og.grid(row=0, column=0, padx=20, pady=5, sticky="ew")

def delete():
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"The file '{output_file}' has been deleted.")
    else:
        print(f"The file '{output_file}' does not exist.")

app = customtkinter.CTk()
app.title("Background Removal")
app.geometry("800x1000")
app.grid_columnconfigure((0), weight=1)

title = customtkinter.CTkLabel(app, text="Background Removal", corner_radius = 5, font = (None, 35), anchor = "center")
title.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

path = customtkinter.CTkEntry(app, placeholder_text="Browse Image or Put the Path in this Box")
path.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

button = customtkinter.CTkButton(app, text="Browse Image", command=open_file, anchor = "center")
button.grid(row=2, column=0, padx=20, pady=5)

button1 = customtkinter.CTkButton(app, text="Process", command=process)
button1.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

tabview = customtkinter.CTkTabview(app, width=400, height=400)
og_tab = tabview.add("Original")
bg_tab = tabview.add("No Background")
tabview.grid(row=4, column=0, padx=20, pady=5)

button2 = customtkinter.CTkButton(app, text="Delete No Background Image", command=delete, fg_color = "#B31312",hover_color = "#F24C3D", anchor = "center")
button2.grid(row=5, column=0, pady=15)

app.mainloop()
