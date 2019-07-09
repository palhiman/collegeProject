from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2
from tkinter import messagebox


# functions
# selecting image
def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    panelA = None
    panelB = None

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
            panelA = Label(frame1, image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            panelB = Label(frame2, image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)


        #otherwise, update the image panels
        else:
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged




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

# Exitinnng the application
def exit_application():
    if messagebox.askokcancel("Exitinnnng!!!"):
        f = Text("Bye Bye ...:w")
        f.pack()
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


# Main window container
root = Tk()
root.geometry("870x600")

# menubar
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
#datamenu.add_command(label="MNIST")
#datamenu.add_command(label="ImageNet")
#datamenu.add_command(label="CIFAR-10")
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
#algomenu.add_command(label="Niblack's")
algomenu.add_command(label="Sauvola's")
#algomenu.add_command(label="Canny Edge Detection")
menubar.add_cascade(label="Algorithms", menu=algomenu)

# help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Documentation", command=documentation)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)


# frame 1 to hold input image
frame1 = Frame(root)
frame1.pack(side=LEFT, padx=20)


# frame 2 to hold output image
frame2 = Frame(root)
frame2.pack(side=LEFT)

# Buttons
# adding button for browsing image in the local drive
frame = Frame(root)
frame.pack(side=BOTTOM, padx=None)

btn = Button(frame, text="Browse Image", command=select_image)
btn.pack(side=LEFT, padx=10, pady=10)

btn1 = Button(frame, text="Algorithm", command=algorithm)
btn1.pack(side=LEFT, padx=10, pady=10)

btn1 = Button(frame, text="Morphology", command=morphology)
btn1.pack(side=LEFT, padx=10, pady=10)

btn2 = Button(frame, text="Reshaping Vector", command=reshaping)
btn2.pack(side=LEFT, padx=10, pady=10)

btn3 = Button(frame, text="Train/Test", command=train_test)
btn3.pack(side=LEFT, padx=10, pady=10)

################



root.config(menu=menubar)
root.mainloop()