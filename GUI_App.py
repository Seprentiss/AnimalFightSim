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
    if Animal_One_Selection.get() == "Gorilla":
        Imglft = ImageTk.PhotoImage(file="Images/Gorilla.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Grizzly Bear":
        Imglft = ImageTk.PhotoImage(file="Images/Grizzly.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Polar Bear":
        Imglft = ImageTk.PhotoImage(file="Images/Polar_Bear.jpg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Bison":
        Imglft = ImageTk.PhotoImage(file="Images/Bison.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Bull":
        Imglft = ImageTk.PhotoImage(file="Images/Bull.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Tiger":
        Imglft = ImageTk.PhotoImage(file="Images/Tiger.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Lion":
        Imglft = ImageTk.PhotoImage(file="Images/Lion.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Moose":
        Imglft = ImageTk.PhotoImage(file="Images/Moose.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Hippo":
        Imglft = ImageTk.PhotoImage(file="Images/Hippo.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Giraffe":
        Imglft = ImageTk.PhotoImage(file="Images/Giraffe.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Elephant":
        Imglft = ImageTk.PhotoImage(file="Images/Elephant.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Cougar":
        Imglft = ImageTk.PhotoImage(file="Images/Cougar.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Jaguar":
        Imglft = ImageTk.PhotoImage(file="Images/Jaguar.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Chimp":
        Imglft = ImageTk.PhotoImage(file="Images/Chimp.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Wolf":
        Imglft = ImageTk.PhotoImage(file="Images/Wolf.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft
    if Animal_One_Selection.get() == "Rhino":
        Imglft= ImageTk.PhotoImage(file="Images/Rhino.jpeg")
        label_left.configure(image=Imglft)
        label_left.image = Imglft

def ComboBoxImageRight():
    if Animal_Two_Selection.get() == "Gorilla":
        ImgRgt = ImageTk.PhotoImage(file="Images/Gorilla.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Grizzly Bear":
        ImgRgt = ImageTk.PhotoImage(file="Images/Grizzly.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Polar Bear":
        ImgRgt = ImageTk.PhotoImage(file="Images/Polar_Bear.jpg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Bison":
        ImgRgt = ImageTk.PhotoImage(file="Images/Bison.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Bull":
        ImgRgt = ImageTk.PhotoImage(file="Images/Bull.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Tiger":
        ImgRgt = ImageTk.PhotoImage(file="Images/Tiger.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Lion":
        ImgRgt = ImageTk.PhotoImage(file="Images/Lion.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Moose":
        ImgRgt = ImageTk.PhotoImage(file="Images/Moose.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Hippo":
        ImgRgt = ImageTk.PhotoImage(file="Images/Hippo.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Giraffe":
        ImgRgt = ImageTk.PhotoImage(file="Images/Giraffe.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Elephant":
        ImgRgt = ImageTk.PhotoImage(file="Images/Elephant.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Cougar":
        ImgRgt = ImageTk.PhotoImage(file="Images/Cougar.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Jaguar":
        ImgRgt = ImageTk.PhotoImage(file="Images/Jaguar.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Chimp":
        ImgRgt = ImageTk.PhotoImage(file="Images/Chimp.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Wolf":
        ImgRgt = ImageTk.PhotoImage(file="Images/Wolf.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt
    if Animal_Two_Selection.get() == "Rhino":
        ImgRgt = ImageTk.PhotoImage(file="Images/Rhino.jpeg")
        label_right.configure(image=ImgRgt)
        label_right.image = ImgRgt

def Start(anOne, anTwo, Terrain):
    global output, num_of_tests, terrain
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

app = tk.Tk()

app_width = 1000
app_height = 600

app['bg'] = 'grey'

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
app.title("Animal Fight Simulator")
app.anchor("n")

labelTop = tk.Label(app,
                    text="Choose 2 animals and 1 terrain")
labelTop.pack()

Animal_One_Start_Animals = List()
Animal_One_Start_Animals.remove("Grizzly Bear")

Animal_One_Selection = ttk.Combobox(app,values=Animal_One_Start_Animals)
Animal_One_Selection.bind("<<ComboboxSelected>>", Handler1)
Animal_One_Selection.pack()
Animal_One_Selection.current(0)

Animal_Two_Start_Animals = List()
Animal_Two_Start_Animals.remove("Gorilla")

Animal_Two_Selection = ttk.Combobox(app,values=Animal_Two_Start_Animals)
Animal_Two_Selection.bind("<<ComboboxSelected>>", Handler2)
Animal_Two_Selection.pack()
Animal_Two_Selection.current(0)


Terrain_Selction = ttk.Combobox(app,values=terrain)
Terrain_Selction.pack()
Terrain_Selction.current(0)


tk.Button(app,text="Start", command=lambda: (Start(Animal_One_Selection, Animal_Two_Selection, Terrain_Selction)), width=20).pack()
text = tk.Text(height = 10, width = 30)
myFont = font.Font(size= 20, weight="bold")
text["font"] = myFont
text.insert(tk.END, "Result of Sim will appear here")
text.pack()

Imglft = ImageTk.PhotoImage(file="Images/Gorilla.jpeg")
label_left = ttk.Label(app, image=Imglft)
label_left.place(relx=0, rely=.3, anchor="w")

ImgRgt = ImageTk.PhotoImage(file="Images/Grizzly.jpeg")
label_right = ttk.Label(app, image=ImgRgt)
label_right.place(relx=1, rely=.3, anchor="e")

def on_click(text_to_add):
    text.delete('1.0', tk.END)
    text.insert("0.0", str(text_to_add))

app.mainloop()



