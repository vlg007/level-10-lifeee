from tkinter import *
from PIL import Image, ImageTk
import pathlib, os
import math

class CircleFrame():
    def __init__(self, sliceImage, sliceRating):
        global nextFrame
        nextFrame = ""
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
        frameM = Frame(width=900, height=800, bg="white")
        self.spriteLibrary = []
        # this was moved since python is really weird with how it accepts __file__, almost every issue I had was literally either change an argument or move a line
        self.current_dir = pathlib.Path(__file__).parent.resolve()

    # modify the new circle by basically redoing the entire setup, but with the new sliceRating
    def modify(self, newAverage):
        MainCircle.canvasM.destroy()
        self.createSlicesM()
        s1.sliceRating = str(int(newAverage))
        self.createCircle(len(self.spriteLibrary))
        frameM.pack(side="left")
        print(newAverage)
        print(s1.sliceRating)

    # create the main pie slice objects
    def createSlicesM(self):
        global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
        s1 = CircleFrame("10_Pie_Slice_r", "0")
        s2 = CircleFrame("10_Pie_Slice_m", "0")
        s3 = CircleFrame("10_Pie_Slice_fit", "0")
        s4 = CircleFrame("10_Pie_Slice_c", "0")
        s5 = CircleFrame("10_Pie_Slice_free", "0")
        s6 = CircleFrame("10_Pie_Slice_k", "0")
        s7 = CircleFrame("10_Pie_Slice_fri", "0")
        s8 = CircleFrame("10_Pie_Slice_sc", "0")
        s9 = CircleFrame("10_Pie_Slice_fa", "0")
        s10 = CircleFrame("10_Pie_Slice_fi", "0")

    # create a list for easy recall
    def createCircle(self, val):
        sliceList = [s3, s4, s5, s6, s7, s8, s9, s10, s1, s2]

        # generate the canvas
        MainCircle.canvasM = Canvas(frameM, width=900, height=800, bg="white")
        MainCircle.canvasM.pack()

        # create the test button
        category1 = Button(MainCircle.canvasM, font="Palatino_Linotype", text="Romance", fg="Red", bg="White", relief="flat", command=self.generateSide1)
        category1.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(600, 100, window=category1, anchor="nw")

        # generate the images
        for i in range(len(sliceList)):
            directory = sliceList[i].sliceImage + sliceList[i].sliceRating + ".png"
            img_path = os.path.join(self.current_dir, directory)
            sprite = ImageTk.PhotoImage(file=img_path)
            # save the images to a list so that they can all display at the same time
            self.spriteLibrary.append(sprite)
            MainCircle.canvasM.image = sprite
            print(img_path)
            print(len(self.spriteLibrary))
            # place the images down, set up to be arranged in a circle, utilizing the rotation forumla. (The images are STILL WIP so they might not fit entirely)
            MainCircle.canvasM.create_image(((120 * math.cos(math.radians(36*i))) + (120 * math.sin(math.radians(36*i)))) + 100,((120 * math.sin(math.radians(36*i))) - (120 * math.cos(math.radians(-36*i)))) + 150,image=self.spriteLibrary[i + val], anchor="nw")
            frameM.pack(side="left")

    # generate the circle
    def generateMain(self):
        self.createSlicesM()
        self.createCircle(0)

    # swap to the second circle
    def generateSide1(self):
        frameM.pack_forget()
        SideCircle1.createSlices1(self)



class SideCircle1():
    def __init__(self, the_window):
        global frame2, prevRatings
        frame2 = Frame(width=900, height=800, bg="white")
        self.spriteLibrary2 = []
        # this is the lineup for all the ratings in each subcategory
        prevRatings = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

    # set each rating to its corresponding category
    def rateList(self, prevRatings, buttonNum, sliceGroup):
        rat = prevRatings[sliceGroup]
        if (rat != buttonNum) :
            prevRatings[sliceGroup] = buttonNum
        elif (buttonNum == rat):
            prevRatings[sliceGroup] = 0

    # calculate the rating average and go back to the main function
    def goBackToMain(self, prevRatings, frame, s):
        average = 0
        for i in range(len(prevRatings)):
            print(prevRatings[str(i+1)])
            average += prevRatings[str(i+1)]
        print(average)
        average /= len(prevRatings)
        print(average)
        frame.pack_forget()
        create.modify(average)

    # create the slices similar to the main circle
    def createSlices1(self):
        frame2.pack(side="left")


        canvas1 = Canvas(frame2, width=900, height=800, bg="white")
        canvas1.pack()

        # set up buttons for EVERY rating, and have them call the rateList function
        Button7 = Button(canvas1, font="Palatino_Linotype", text="7", relief="flat", fg="Red", bg="White", command= lambda: create3.rateList(prevRatings, 7, '1'))
        Button7.pack(padx=0, pady=0)
        canvas1.create_window(500, 100, window=Button7, anchor="nw")

        Button23 = Button(canvas1, font="Palatino_Linotype", text="3", relief="flat", fg="Red", bg="White", command= lambda: create3.rateList(prevRatings, 3, '3'))
        Button23.pack(padx=0, pady=0)
        canvas1.create_window(400, 100, window=Button23, anchor="nw")

        Button35 = Button(canvas1, font="Palatino_Linotype", text="5", relief="flat", fg="Red", bg="White", command= lambda: create3.rateList(prevRatings, 5, '4'))
        Button35.pack(padx=0, pady=0)
        canvas1.create_window(700, 100, window=Button35, anchor="nw")


        backButton = Button(canvas1, font="Palatino_Linotype", text="Back", relief="groove", fg="Black", command= lambda: create3.goBackToMain(prevRatings, frame2, 8))
        backButton.pack()
        canvas1.create_window(600, 100, window=backButton, anchor="nw")


# create the text frame :]
class TextFrame():
    def __init__(self, the_window):
        frame2 = Frame(width=200, height=800, bg="grey")
        frame2.pack(side="right")
        canvas2 = Canvas(frame2, width=200, height=800, bg="grey")
        canvas2.pack()
        

###################################################################
# Main Program
###################################################################

# window is weird atm since the current image sizes have not been tweaked to fit yet
width = 1100
height = 800

window = Tk()
window.geometry("{}x{}".format(width, height))
window.title("Level 10 Life")

create = MainCircle(window)
create2 = TextFrame(window)
create3 = SideCircle1(window)
create.generateMain()

window.mainloop
