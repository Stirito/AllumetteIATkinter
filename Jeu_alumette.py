import tkinter as tk
from PIL import Image, ImageTk

class MyWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Window")
        image = Image.open("background.jpg")
        self.root.geometry(str(image.height)+"x"+str(image.width))
        # Load the image
        self.l = Liste_Alumette(10)
        
        background_image = ImageTk.PhotoImage(image)
       
        
        
        # Create a label with the image as the background
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Other widgets and code for your window
        self.l.Afficher(self.root)
        self.root.mainloop()
class Alumette:
    def __init__(self) -> None:
        self.image = Image.open("alumettes.png")
      
class Liste_Alumette:
    def __init__(self,n) -> None:
        self.liste_alumette = [Alumette() for i in range(n)]
    def Afficher(self,root):
        for alumette in self.liste_alumette:
            photo = ImageTk.PhotoImage(alumette.image.resize((100,200)))
            label = tk.Label(root, image = photo)
            label.image = photo
            label.grid(row=0,column=self.liste_alumette.index(alumette))
# Create an instance of the window
window = MyWindow()
