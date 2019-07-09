#!/usr/bin/env python3

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2
from tkinter import messagebox

def select_image():
    # grab a reference to the image panels
    global panelA, panelB

    path = tkinter.filedialog.askopenfilename()
    #
    #ensures a file path was selected
    if len(path) > 0:
        # load an from disk, covert to grayscale & detect edges
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)

        # OpenCV represents images in BGR order, whereas
        # PIL represents images in RGB order
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        # if the panel are None, initialize them
        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)


        #otherwise, update the image panels
        else:
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged

# Exitinnng the application
def exit_application():
    if messagebox.askokcancel("Exitinnnng!!!"):
        root.destroy()


def documentation():
    pass

def about():
    about_the_application = """ 
    <><><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    .....This is application is under development .....\n
    The whole idea of developing this application is to get understanding of two domains on which\n
    this project is based on i.e. Image Processing and Deep Learning....
    
    <><><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>       
    """
    print(about_the_application)

# root window for the Application
root = Tk()
root.title("Inpainting of Degraded documentation using Convolutional Neural Network")
#root.geometry("650x450")

# definition for all the algorithms
def algorithm():
    pass

# performing morphology
def morphology():
    pass

# reshaping of vectors
def reshaping():
    pass

# training and testing the images
def train_test():
    pass


panelA = None
panelB = None

# filemenu
menubar = Menu(root)

# file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=select_image)
#filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_application)
menubar.add_cascade(label="File", menu=filemenu)

# dataset menu
datamenu = Menu(menubar, tearoff=0)
datamenu.add_command(label="DIBCO")
datamenu.add_command(label="MNIST")
datamenu.add_command(label="ImageNet")
datamenu.add_command(label="CIFAR-10")
menubar.add_cascade(label="Datasets", menu=datamenu)

# Tools used menu menu
toolmenu = Menu(menubar, tearoff=0)
toolmenu.add_command(label="Numpy")
toolmenu.add_command(label="Scikit-Learn")
toolmenu.add_command(label="Scikit-Image")
toolmenu.add_command(label="Keras")
toolmenu.add_command(label="Tensorflow")
menubar.add_cascade(label="Tools", menu=toolmenu)

# Applied Algorithm
algomenu = Menu(menubar, tearoff=0)
algomenu.add_command(label="Otsu's Thresholding")
algomenu.add_command(label="Niblack's")
algomenu.add_command(label="Sauvola's")
algomenu.add_command(label="Canny Edge Detection")
menubar.add_cascade(label="Algorithms", menu=algomenu)

# help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Documentation", command=documentation)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)


# adding button for browsing image in the local drive
btn = Button(root, text="Browse Image", command=select_image)
btn.pack( padx=10, pady=10)

btn1 = Button(root, text="Algorithm", command=algorithm)
btn1.pack( padx=10, pady=10)

btn1 = Button(root, text="Morphology", command=morphology)
btn1.pack( padx=10, pady=10)

btn2 = Button(root, text="Reshaping Vector", command=reshaping)
btn2.pack( padx=10, pady=10)

btn3 = Button(root, text="Train/Test", command=train_test)
btn3.pack( padx=10, pady=10)

root.config(menu=menubar)
root.mainloop()


