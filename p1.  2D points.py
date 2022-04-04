# import tkinter for the gui and PIL so we can use png and jpg files
from tkinter import *
from PIL import Image, ImageTk

# create the main circle frame
class CircleFrame():
    def __init__(self, the_window):
        frame1 = Frame(width=400, height=400, bg="white")
        frame1.grid(row=0, column=0)
        # create a canvas that the main circle will be drawn onto
        canvas1 = Canvas(frame1, width=400, height=400, bg="blue")
        # make sure that it is placed ON the frame, and doesn't impact the grid
        canvas1.pack()
        # take the image and place it onto a variable
        sprite1 = ImageTk.PhotoImage(file=r"Slice_image_placeholder.png")
        # reference said image so it doesn't get garbage collected
        canvas1.image = sprite1
        # generate the image onto the canvas
        canvas1.create_image(200,200,image=sprite1)


# this is the same as the CircleFrame, but with no canvas since this will be entirely text & button-based
class TextFrame():
    def __init__(self, the_window):
        frame2 = Frame(width=350, height=400, bg="grey")
        frame2.grid(row=0, column=1)



###################################################################
# Main Program
###################################################################

# set default window size
width = 750
height = 400

# set up the gui
window = Tk()
window.geometry("{}x{}".format(width, height))
window.title("Placeholder Name")

# call the classes and generate the widgets
create = CircleFrame(window)
create2 = TextFrame(window)

window.mainloop





