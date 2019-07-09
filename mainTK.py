#!/usr/bin/env python3

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2
from tkinter import messagebox
from documentation import Documentation
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from skimage import exposure
#%matplotlib inline



def select_image():
    # grab a reference to the image panels
    global panelA, panelB, path
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

# definition for all the algorithms
def algorithm1():
    img = cv2.imread(path,0)
    #blur = cv2.GaussianBlur(img,(5,5),0)
     
    # find normalized_histogram, and its cumulative distribution functio
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_norm = hist.ravel()/hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in range(1,256):
        p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
        q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
    if q1 == 0:
        q1 = 0.00000001
    if q2 == 0:
        q2 = 0.00000001
    b1,b2 = np.hsplit(bins,[i]) # weights
     # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
     # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
    # find otsu's threshold value with OpenCV function
    ret, otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print("Final thresholding values:")
    print (thresh,ret)

# performing 
def algorithm():
    img = cv2.imread(path,0)
 
    ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
     
    plt.subplot(3,1,1)
    plt.imshow(img,cmap = 'gray')
    plt.title('Original Noisy Image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(3,1,2)
    plt.hist(img.ravel(), 256)
    plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
    plt.title('Histogram')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(3,1,3)
    plt.imshow(imgf,cmap = 'gray')
    plt.title('Otsu thresholding')
    plt.xticks([])
    plt.yticks([])
    plt.show()   

# reshaping of vectors
def reshaping():
    img = plt.imread(path)
    print(img.shape)

    vec = np.asarray(img) # converting image as array
    print(vec)


# training and testing the images
def train_test():
    pass


# root window for the Application
root = Tk()
root.title("Inpainting of Degraded documentation using Convolutional Neural Network")
root.geometry("850x550")


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



# adding button for browsing image in the local drive
frame = Frame(root)
frame.pack(side=BOTTOM)

btn = Button(frame, text="Browse Image", command=select_image)
btn.pack(side=LEFT, padx=10, pady=10)

btn1 = Button(frame, text="Otsu1", command=algorithm)
btn1.pack(side=LEFT, padx=10, pady=10)

btn1 = Button(frame, text="Otsu 2", command=algorithm1)
btn1.pack(side=LEFT, padx=10, pady=10)

btn2 = Button(frame, text="Reshaping Vector", command=reshaping)
btn2.pack(side=LEFT, padx=10, pady=10)

btn3 = Button(frame, text="Train/Test", command=train_test)
btn3.pack(side=LEFT, padx=10, pady=10)



root.config(menu=menubar)
root.mainloop()


