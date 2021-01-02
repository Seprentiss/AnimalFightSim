import tkinter as tk
import Images
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font as font
from SIMS import PLAINS, Jungle, Arctic, Desert, All_Sims

def List():
    return ["Gorilla",
        "Grizzly Bear",
        "Polar Bear",
        "Tiger",
        "Lion",
        "Elephant",
        "Hippo",
        "Rhino",
        "Bull",
        "Bison",
        "Chimp",
        "Jaguar",
        "Cougar",
        "Moose",
        "Giraffe",
        "Wolf"]

terrain = ["Plains", "Jungle", "Arctic", "Desert", "All"]
def ComboBoxImageLeft():
    global Imglft
    if Animal_One_Selection.get() == "Gorilla":
        Imglft = ImageTk.PhotoImage(file="Images/Gorilla.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Grizzly Bear":
        Imglft = ImageTk.PhotoImage(file="Images/Grizzly.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Polar Bear":
        Imglft = ImageTk.PhotoImage(file="Images/Polar_Bear.jpg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Bison":
        Imglft = ImageTk.PhotoImage(file="Images/Bison.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Bull":
        Imglft = ImageTk.PhotoImage(file="Images/Bull.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Tiger":
        Imglft = ImageTk.PhotoImage(file="Images/Tiger.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Lion":
        Imglft = ImageTk.PhotoImage(file="Images/Lion.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Moose":
        Imglft = ImageTk.PhotoImage(file="Images/Moose.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Hippo":
        Imglft = ImageTk.PhotoImage(file="Images/Hippo.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Giraffe":
        Imglft = ImageTk.PhotoImage(file="Images/Giraffe.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Elephant":
        Imglft = ImageTk.PhotoImage(file="Images/Elephant.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Cougar":
        Imglft = ImageTk.PhotoImage(file="Images/Cougar.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Jaguar":
        Imglft = ImageTk.PhotoImage(file="Images/Jaguar.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Chimp":
        Imglft = ImageTk.PhotoImage(file="Images/Chimp.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Wolf":
        Imglft = ImageTk.PhotoImage(file="Images/Wolf.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)
    if Animal_One_Selection.get() == "Rhino":
        Imglft= ImageTk.PhotoImage(file="Images/Rhino.jpeg")
        canvas.itemconfigure(ImLEFT, image = Imglft)

def ComboBoxImageRight():
    global ImgRgt
    if Animal_Two_Selection.get() == "Gorilla":
        ImgRgt = ImageTk.PhotoImage(file="Images/Gorilla.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Grizzly Bear":
        ImgRgt = ImageTk.PhotoImage(file="Images/Grizzly.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Polar Bear":
        ImgRgt = ImageTk.PhotoImage(file="Images/Polar_Bear.jpg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Bison":
        ImgRgt = ImageTk.PhotoImage(file="Images/Bison.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Bull":
        ImgRgt = ImageTk.PhotoImage(file="Images/Bull.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Tiger":
        ImgRgt = ImageTk.PhotoImage(file="Images/Tiger.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Lion":
        ImgRgt = ImageTk.PhotoImage(file="Images/Lion.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Moose":
        ImgRgt = ImageTk.PhotoImage(file="Images/Moose.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Hippo":
        ImgRgt = ImageTk.PhotoImage(file="Images/Hippo.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Giraffe":
        ImgRgt = ImageTk.PhotoImage(file="Images/Giraffe.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Elephant":
        ImgRgt = ImageTk.PhotoImage(file="Images/Elephant.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Cougar":
        ImgRgt = ImageTk.PhotoImage(file="Images/Cougar.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Jaguar":
        ImgRgt = ImageTk.PhotoImage(file="Images/Jaguar.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Chimp":
        ImgRgt = ImageTk.PhotoImage(file="Images/Chimp.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Wolf":
        ImgRgt = ImageTk.PhotoImage(file="Images/Wolf.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)
    if Animal_Two_Selection.get() == "Rhino":
        ImgRgt = ImageTk.PhotoImage(file="Images/Rhino.jpeg")
        canvas.itemconfigure(ImRIght, image = ImgRgt)

def BackGroundSelection(event):
    global Imgback
    if Terrain_Selction.get() == "Plains":
        Imgback = ImageTk.PhotoImage(Image.open("Images/Plains.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        canvas.itemconfigure(bg, image=Imgback)
    if Terrain_Selction.get() == "Jungle":
        Imgback = ImageTk.PhotoImage(Image.open("Images/Jungle.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        canvas.itemconfigure(bg, image=Imgback)
    if Terrain_Selction.get() == "Arctic":
        Imgback = ImageTk.PhotoImage(Image.open("Images/Arctic.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        canvas.itemconfigure(bg, image=Imgback)
    if Terrain_Selction.get() == "Desert":
        Imgback = ImageTk.PhotoImage(Image.open("Images/Desert.jpeg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        canvas.itemconfigure(bg, image=Imgback)
    if Terrain_Selction.get() == "All":
        Imgback = ImageTk.PhotoImage(Image.open("Images/All.jpg").resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        canvas.itemconfigure(bg, image=Imgback)
def Start(anOne, anTwo, Terrain):
    global output, num_of_tests, terrain
    num_of_tests = 1000
    if Terrain.get() == "Plains":
        output = PLAINS.PlainsSim(str(anOne.get()).title(), str(anTwo.get()).title())
    if Terrain.get() == "Jungle":
        output = Jungle.JungleSim(anOne.get().title(), anTwo.get().title())
    if Terrain.get() == "Arctic":
        output = Arctic.ArcticSim(anOne.get().title(), anTwo.get().title())
    if Terrain.get() == "Desert":
        output = (Desert.DesertSim(anOne.get().title(), anTwo.get().title()))
    if Terrain.get() == "All":
        output = (All_Sims.AllSim(anOne.get().title(), anTwo.get().title()))
    if output[0] > output[1]:
        if Terrain.get() == "All":
            num_of_tests = num_of_tests * (len(terrain) - 1)
        winP = float(output[0] / (num_of_tests / 100))
        on_click("The " + str(anOne.get())  + " Wins:" + "\nThey Won " + str(
            winP) + "% of the Match-ups")
    if output[1] > output[0]:
        if Terrain.get() == "All":
            num_of_tests = num_of_tests * (len(terrain) - 1)
        winP = float(output[1] / (num_of_tests / 100))
        on_click("The " + str(anTwo.get()) + " Wins:" + "\nThey Won " + str(
            round(winP, 2)) + "% of the Match-ups")


def updt_An_1_Animals():
    a = List()
    word = str(Animal_One_Selection.get())
    indx = a.index(word)
    a.pop(indx)
    Animal_Two_Selection["values"] = a

def updt_An_2_Animals():
    b = List()
    word = str(Animal_Two_Selection.get())
    indx = b.index(word)
    b.pop(indx)
    Animal_One_Selection["values"] = b

def Handler1(event):
    updt_An_1_Animals()
    ComboBoxImageLeft()
def Handler2(event):
    updt_An_2_Animals()
    ComboBoxImageRight()

IMAGE_PATH = 'Images/Plains.jpg'
WIDTH, HEIGHT = 1200, 800

app = tk.Tk()
app.resizable(False, False)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)
app.geometry(f'{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}')
app.title("Animal Fight Simulator")
app.anchor("n")


canvas = tk.Canvas(app, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both", expand=True)

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)


ttk.Style().configure('green/black.TLabel', foreground='black', background='black')
ttk.Style().configure('black/black.TButton', foreground='black', background='black')

# Put a tkinter widget on the canvas.
button = ttk.Button(app,text="Start", style='green/black.TButton', command=lambda: (Start(Animal_One_Selection, Animal_Two_Selection, Terrain_Selction)), width=20)
button_window = canvas.create_window(600, 600, anchor='c', window=button)

Animal_One_Start_Animals = List()
Animal_One_Start_Animals.remove("Grizzly Bear")

Animal_One_Selection = ttk.Combobox(app,values=Animal_One_Start_Animals)
Animal_One_Selection.bind("<<ComboboxSelected>>", Handler1)
Animal_One_Selection.current(0)
combo_window = canvas.create_window(350, 500, anchor='c', window=Animal_One_Selection)

Animal_Two_Start_Animals = List()
Animal_Two_Start_Animals.remove("Gorilla")

Animal_Two_Selection = ttk.Combobox(app,values=Animal_Two_Start_Animals,  style='green/black.TCombobox')
Animal_Two_Selection.bind("<<ComboboxSelected>>", Handler2)
Animal_Two_Selection.current(0)
combo_window2 = canvas.create_window(850, 500, anchor='c', window=Animal_Two_Selection)


Terrain_Selction = ttk.Combobox(app,values=terrain)
Terrain_Selction.bind("<<ComboboxSelected>>", BackGroundSelection)
Terrain_Selction.current(0)

combo_window3 = canvas.create_window(600, 500, anchor='c', window=Terrain_Selction)

one = ImageTk.PhotoImage(file=r'Images/Gorilla.jpeg')
app.one = one  # to prevent the image garbage collected.
ImLEFT = canvas.create_image((200,300), image=one, anchor='c')

two = ImageTk.PhotoImage(file=r'Images/Grizzly.jpeg')
app.two = two  # to prevent the image garbage collected.
ImRIght = canvas.create_image((1000,300), image=two, anchor='c')


labelTop = tk.Label(app,
                    text="Choose 2 animals and 1 terrain")
labelTop_window = canvas.create_text(600, 100, anchor='c', text="Choose 2 animals and 1 terrain", fill= "black", font=('Arial',30,'bold italic'))




text = tk.Text(height = 10, width = 25)
myFont = font.Font(size= 20, weight="bold")
text["font"] = myFont
text.insert(tk.END, "Result of Sim will appear here")
text_window = canvas.create_window(600,300,anchor='c', window=text)


def on_click(text_to_add):
    text.delete('1.0', tk.END)
    text.insert("0.0", str(text_to_add))

app.mainloop()

