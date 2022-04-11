from tkinter import *
from PIL import Image, ImageTk
import pathlib, os
import math

class CircleFrame():
    def __init__(self, sliceName, sliceImage, sliceRating="0"):
        self.sliceName = sliceName
        self.sliceImage = sliceImage
        self.sliceRating = sliceRating

    @property
    def sliceName(self):
        return self._sliceName

    @sliceName.setter
    def sliceName(self, value):
        self._sliceName = value

    @property
    def sliceImage(self):
        return self._sliceImage

    @sliceImage.setter
    def sliceImage(self, value):
        self._sliceImage = value

    @property
    def sliceRating(self):
        return self._sliceRating

    @sliceRating.setter
    def sliceRating(self, value):
        self._sliceRating = value

class MainCircle():
    def __init__(self, the_window):
        global frameM
        frameM = Frame(width=700, height=800, bg="white")
        frameM.grid(row=0, column=0)
        self.spriteLibrary = []

    # create the main pie slice objects
    def createSlices(self):
        s1 = CircleFrame("Romance", "10_Pie_Slice_r")
        s2 = CircleFrame("Mindset", "10_Pie_Slice_m")
        s3 = CircleFrame("Fitness", "10_Pie_Slice_fit")
        s4 = CircleFrame("Career", "10_Pie_Slice_c")
        s5 = CircleFrame("Free Time", "10_Pie_Slice_free")
        s6 = CircleFrame("Karma", "10_Pie_Slice_k")
        s7 = CircleFrame("Friends", "10_Pie_Slice_fri")
        s8 = CircleFrame("Self Care", "10_Pie_Slice_sc")
        s9 = CircleFrame("Family", "10_Pie_Slice_fa")
        s10 = CircleFrame("Finance", "10_Pie_Slice_fi")
        sliceList = [s3, s4, s5, s6, s7, s8, s9, s10, s1, s2]

        # demonstrate that the differentiating images works
        s1.sliceRating = "1"
        s2.sliceRating = "2"
        s3.sliceRating = "3"
        s4.sliceRating = "4"
        s5.sliceRating = "5"
        s6.sliceRating = "6"
        s7.sliceRating = "7"
        s8.sliceRating = "8"
        s9.sliceRating = "9"
        s10.sliceRating = "10"

        # generate the canvas
        MainCircle.canvasM = Canvas(frameM, width=700, height=800, bg="white")
        MainCircle.canvasM.pack()

        # generate the images
        for i in range(len(sliceList)):
            current_dir = pathlib.Path(__file__).parent.resolve()
            directory = sliceList[i].sliceImage + sliceList[i].sliceRating + ".png"
            img_path = os.path.join(current_dir, directory)
            sprite = ImageTk.PhotoImage(file=img_path)
            # save the images to a list so that they can all display at the same time
            self.spriteLibrary.append(sprite)
            MainCircle.canvasM.image = sprite
            # place the images down, set up to be arranged in a circle, utilizing the rotation forumla. (The images are STILL WIP so they might not fit entirely)
            MainCircle.canvasM.create_image(((200 * math.cos(math.radians(-36*i))) + (100 * math.sin(math.radians(36*i)))) + 350,((200 * math.sin(math.radians(36*i))) - (100 * math.cos(math.radians(-36*i)))) + 425,image=self.spriteLibrary[i])


    def generate(self):
        self.createSlices()



class SideCircles(MainCircle):
    def __init__(self, the_window):
        global frame2
        frame2 = Frame(width=700, height=800, bg="white")
        frame2.grid(row=0, column=0)
        self.spriteLibrary2 = []

    def createSlices2(self):
        sa1 = CircleFrame("Current Relationship", "Placeholder")
        sa2 = CircleFrame("Trustworthiness", "Placeholder")
        sa3 = CircleFrame("Love for Partner", "Placeholder")
        sa4 = CircleFrame("Meeting People", "Placeholder")
        sa5 = CircleFrame("General", "Placeholder")


class TextFrame():
    def __init__(self, the_window):
        frame2 = Frame(width=200, height=800, bg="grey")
        frame2.grid(row=0, column=1)
        canvas2 = Canvas(frame2, width=350, height=400, bg="grey")
        canvas2.pack()
        


###################################################################
# Main Program
###################################################################

# window is weird atm since the current image sizes have not been tweaked to fit yet
width = 900
height = 800

window = Tk()
window.geometry("{}x{}".format(width, height))
window.title("Level 10 Life")

create = MainCircle(window)
create2 = TextFrame(window)
create.generate()

window.mainloop




