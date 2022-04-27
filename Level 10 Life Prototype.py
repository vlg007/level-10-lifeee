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
        self.current_dir = pathlib.Path(__file__).parent.resolve()

    # modify the new circle by basically redoing the entire setup, but with the new sliceRating
    def returning(self):
        MainCircle.canvasM.destroy()
        self.createSlicesM()
        self.createCircle(len(self.spriteLibrary))
        frameM.pack(side="left")

    # create the main pie slice objects
    def createSlicesM(self):
        global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
        s1 = CircleFrame("10_Pie_Slice_r", str(int(averages["1"])))
        s2 = CircleFrame("10_Pie_Slice_m", str(int(averages["2"])))
        s3 = CircleFrame("10_Pie_Slice_fit", str(int(averages["3"])))
        s4 = CircleFrame("10_Pie_Slice_c", str(int(averages["4"])))
        s5 = CircleFrame("10_Pie_Slice_free", str(int(averages["5"])))
        s6 = CircleFrame("10_Pie_Slice_k", str(int(averages["6"])))
        s7 = CircleFrame("10_Pie_Slice_fri", str(int(averages["7"])))
        s8 = CircleFrame("10_Pie_Slice_sc", str(int(averages["8"])))
        s9 = CircleFrame("10_Pie_Slice_fa", str(int(averages["9"])))
        s10 = CircleFrame("10_Pie_Slice_fi", str(int(averages["10"])))

    # create a list for easy recall
    def createCircle(self, val):
        global sliceList
        sliceList = [s3, s4, s5, s6, s7, s8, s9, s10, s1, s2]

        # generate the canvas
        MainCircle.canvasM = Canvas(frameM, width=900, height=800, bg="white")
        MainCircle.canvasM.pack()

        # create the buttons
        category1 = Button(MainCircle.canvasM, font="Palatino_Linotype", text="Romance", fg="Red", bg="White", relief="groove", command= lambda: self.generateSide(5, "r"))
        category1.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(200, 100, window=category1, anchor="nw")

        category2 = Button(MainCircle.canvasM, font="Palatino_Linotype", text="Mindset", fg="Yellow", bg="Grey", relief="groove", command= lambda: self.generateSide(6, "m"))
        category2.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(400, 100, window=category2, anchor="nw")

        category7 = Button(MainCircle.canvasM, font="Palatino_Linotype", text="Friendship", fg="Pink", bg="Grey", relief="groove", command= lambda: self.generateSide(7, "fri"))
        category7.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(225, 675, window=category7, anchor="nw")

        # generate the images
        
        for i in range(len(sliceList)):
            directory = sliceList[i].sliceImage + sliceList[i].sliceRating + ".png"
            img_path = os.path.join(self.current_dir, directory)
            print(directory)
            print(sliceList[i].sliceRating)
            sprite = ImageTk.PhotoImage(file=img_path)
            sprite = sprite._PhotoImage__photo.subsample(2)
            # save the images to a list so that they can all display at the same time
            self.spriteLibrary.append(sprite)
            MainCircle.canvasM.image = sprite
            print(img_path)
            print(len(self.spriteLibrary))
            # place the images down, set up to be arranged in a circle, utilizing the rotation forumla. (The images are STILL WIP so they might not fit entirely)
            MainCircle.canvasM.create_image(((120 * math.cos(math.radians(36*i))) + (120 * math.sin(math.radians(36*i)))) + 250,\
            ((120 * math.sin(math.radians(36*i))) - (120 * math.cos(math.radians(-36*i)))) + 300,image=self.spriteLibrary[i + val], anchor="nw")
            frameM.pack(side="left")

    # generate the circle
    def generateMain(self):
        self.createSlicesM()
        self.createCircle(0)

    # swap to the second circle
    def generateSide(self, size, category):
        frameM.pack_forget()
        SideCircleR.createSlices1(self, size, category)



class SideCircleR():
    def __init__(self, the_window):
        global frame2, categories, averages
        frame2 = Frame(width=900, height=800, bg="white")
        # this is the lineup for all the ratings in each subcategory
        categories = {}
        self.spritelibrary2 = []
        averages = {str(x+1): 0 for x in range(10)}
        self.current_dir = pathlib.Path(__file__).parent.resolve()

    # set each rating to its corresponding category
    def rateList(self, prevRatings, buttonNum, sliceGroup, category):
        rat = 0
        for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10))):
            rat += categories[("category" + category)][str(i)]
        if ((rat+1) != buttonNum):
            for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10) - (9 - (buttonNum)))):
                categories[("category" + category)][str(i)] = 1
        elif (buttonNum == (rat+1)):
            for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10) - (9 - (buttonNum)))):
                categories[("category" + category)][str(i)] = 0
        print(rat+1)


    def ratingListSetup(self):
        categories["categoryr"] = {str(x+1): 0 for x in range((50))}
        categories["categoryfree"] = {str(x+1): 0 for x in range((50))}
        categories["categoryfa"] = {str(x+1): 0 for x in range((50))}
        categories["categoryfi"] = {str(x+1): 0 for x in range((50))}
        categories["categoryfit"] = {str(x+1): 0 for x in range((50))}
        categories["categoryc"] = {str(x+1): 0 for x in range((60))}
        categories["categorym"] = {str(x+1): 0 for x in range((60))}
        categories["categoryk"] = {str(x+1): 0 for x in range((60))}
        categories["categorysc"] = {str(x+1): 0 for x in range((70))}
        categories["categoryfri"] = {str(x+1): 0 for x in range((70))}

    # calculate the rating average and go back to the main function
    def goBackToMain(self, prevRatings, frame):
        categoriez = ["r", "free", "fa", "fi", "fit", "c", "m", "k", "sc", "fri"]
        for j in range(1, 11):
            for i in range(1, (len(categories[("category" + categoriez[j-1])]) + 1)):
                averages[str(j)] += categories[("category" + categoriez[j-1])][str(i)]
            averages[str(j)] /= (len(categories[("category" + categoriez[j-1])])/10)
        frame.pack_forget()
        create.returning()

    def imagename(self, size, segment, PrevRat, currentRating, libraryIndex, category):
        if (PrevRat == currentRating):
            setting = 0
        elif (PrevRat > currentRating):
            setting = category
        elif (PrevRat < currentRating):
            setting = 0
        directory = "pieslice{}_{}_{}.png".format(size, segment, setting)
        img_path = os.path.join(self.current_dir, directory)
        sprite = ImageTk.PhotoImage(file=img_path)
        sprite = sprite._PhotoImage__photo.subsample(2)
        self.spritelibrary2.append(sprite)
        SideCircleR.canvas1.image = sprite
        print(img_path)
        print(self.spritelibrary2[len(self.spritelibrary2) - 1])
        return self.spritelibrary2[len(self.spritelibrary2) - 1]

    # create the slices similar to the main circle
    def createSlices1(self, size, category):
        frame2.pack(side="left")


        SideCircleR.canvas1 = Canvas(frame2, width=900, height=800, bg="white")
        SideCircleR.canvas1.pack()


        # set up the buttons for the first rating
        Button1_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(10)], 10, 10, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 10, "2", category))
        Button1_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(380, 190, window=Button1_j, anchor="center")

        Button1_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(9)], 9, 9, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 9, "2", category))
        Button1_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(360, 230, window=Button1_i, anchor="center")

        Button1_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(8)], 8, 8, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 8, "2", category))
        Button1_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(340, 270, window=Button1_h, anchor="center")

        Button1_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(7)], 7, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 7, "2", category))
        Button1_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(320, 310, window=Button1_g, anchor="center")

        Button1_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(6)], 6, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 6, "2", category))
        Button1_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(300, 350, window=Button1_f, anchor="center")

        Button1_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(5)], 5, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 5, "2", category))
        Button1_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(280, 390, window=Button1_e, anchor="center")

        Button1_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(4)], 4, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 4, "2", category))
        Button1_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(260, 430, window=Button1_d, anchor="center")

        Button1_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(3)], 3, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 3, "2", category))
        Button1_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(240, 470, window=Button1_c, anchor="center")

        Button1_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(2)], 2, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 2, "2", category))
        Button1_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(220, 510, window=Button1_b, anchor="center")

        Button1_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(1)], 1, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 1, "2", category))
        Button1_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(200, 550, window=Button1_a, anchor="center")



        Button2_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(20)], 10, 10, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 10, "1", category))
        Button2_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(580, 190, window=Button2_j, anchor="center")

        Button2_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(19)], 9, 9, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 9, "1", category))
        Button2_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(560, 230, window=Button2_i, anchor="center")

        Button2_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(18)], 8, 8, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 8, "1", category))
        Button2_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(540, 270, window=Button2_h, anchor="center")

        Button2_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(17)], 7, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 7, "1", category))
        Button2_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(520, 310, window=Button2_g, anchor="center")

        Button2_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(16)], 6, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 6, "1", category))
        Button2_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(500, 350, window=Button2_f, anchor="center")

        Button2_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(15)], 5, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 5, "1", category))
        Button2_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(480, 390, window=Button2_e, anchor="center")

        Button2_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(14)], 4, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 4, "1", category))
        Button2_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(460, 430, window=Button2_d, anchor="center")

        Button2_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(13)], 3, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 3, "1", category))
        Button2_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(440, 470, window=Button2_c, anchor="center")

        Button2_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(12)], 2, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 2, "1", category))
        Button2_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(420, 510, window=Button2_b, anchor="center")

        Button2_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(11)], 1, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(categories[("category" + category)], 1, "1", category))
        Button2_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(400, 550, window=Button2_a, anchor="center")







        backButton = Button(SideCircleR.canvas1, font="Palatino_Linotype", text="Back", relief="groove", fg="Black", command= lambda: create3.goBackToMain(categories[("category" + category)], frame2))
        backButton.pack()
        SideCircleR.canvas1.create_window(100, 100, window=backButton, anchor="nw")
        print(categories[("category" + category)])


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
create3 = SideCircleR(window)
create3.ratingListSetup()
create.generateMain()

window.mainloop
