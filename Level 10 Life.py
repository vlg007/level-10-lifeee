# import everything needed
from tkinter import *
from PIL import ImageTk
import PIL.Image
import pathlib, os
import math
import tkinter.font as font
# import the resources script
from QRCodes import *


# create the object class needed
class CircleFrame():
    def __init__(self, sliceImage, sliceRating):
        # trying to make everything inherit stuff like this just to call it is annoying so we just made certain important variables global
        global nextFrame, deFont
        # define the nextFrame variable
        nextFrame = ""
        # define the image and rating object characteristics
        self.sliceImage = sliceImage
        self.sliceRating = sliceRating
        # define a font for the main circle's buttons
        deFont = font.Font(family="Palatino_Linotype", size=8)

    # define the accessor and mutators
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

# create the main circle 
class MainCircle():
    def __init__(self, the_window):
        global frameM
        # generate the frame for the main circle itself
        frameM = Frame(width=700, height=420, bg="grey")
        # define the image list so the image files can be saved and usedd
        self.spriteLibrary = []
        # define the directory of this program's folder
        self.current_dir = pathlib.Path(__file__).parent.resolve()

    # modify the new circle by basically redoing the entire setup, but with the new sliceRating
    def returning(self):
        # unload the side circle frame
        frame2.pack_forget()
        # destroy the main and side circle canvases
        MainCircle.canvasM.destroy()
        SideCircleR.canvas1.destroy()
        # regenerate the main circle with the new information
        self.createSlicesM()
        self.createCircle(len(self.spriteLibrary))
        frameM.pack(side="left")

    # create the main pie slice objects
    def createSlicesM(self):
        global s1, s2, s3, s4, s5, s6, s7, s8, s9, s10
        # create all of the main circle's category objects
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

    # create the circle itself
    def createCircle(self, val):
        global sliceList
        # create a list with the main slice object names
        # this is in a specific order due to how they are generated
        sliceList = [s3, s4, s5, s6, s7, s8, s9, s10, s1, s2]

        # generate the canvas
        MainCircle.canvasM = Canvas(frameM, width=700, height=420, bg="white")
        MainCircle.canvasM.pack()

        # create the buttons for each category
        category1 = Button(MainCircle.canvasM, font=deFont, text="Romance", fg="#cb0000", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "r"))
        category1.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(200, 30, window=category1, anchor="nw")

        category2 = Button(MainCircle.canvasM, font=deFont, text="Mindset", fg="#fde838", bg="Grey", relief="groove", command= lambda: self.generateSide(6, "m"))
        category2.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(300, 30, window=category2, anchor="nw")

        category3 = Button(MainCircle.canvasM, font=deFont, text="Fitness", fg="#5bf765", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "fit"))
        category3.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(390, 80, window=category3, anchor="nw")

        category4 = Button(MainCircle.canvasM, font=deFont, text="Career", fg="#45baff", bg="Grey", relief="groove", command= lambda: self.generateSide(6, "c"))
        category4.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(420, 175, window=category4, anchor="nw")

        category5 = Button(MainCircle.canvasM, font=deFont, text="Free Time", fg="#1221ff", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "free"))
        category5.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(410, 250, window=category5, anchor="nw")

        category6 = Button(MainCircle.canvasM, font=deFont, text="Karma", fg="#7b16ff", bg="Grey", relief="groove", command= lambda: self.generateSide(6, "k"))
        category6.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(320, 320, window=category6, anchor="nw")

        category7 = Button(MainCircle.canvasM, font=deFont, text="Friendship", fg="#f730ed", bg="Grey", relief="groove", command= lambda: self.generateSide(7, "fri"))
        category7.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(210, 320, window=category7, anchor="nw")

        category8 = Button(MainCircle.canvasM, font=deFont, text="Self Care", fg="#ff1755", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "sc"))
        category8.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(115, 260, window=category8, anchor="nw")

        category9 = Button(MainCircle.canvasM, font=deFont, text="Family", fg="#ff6287", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "fa"))
        category9.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(105, 190, window=category9, anchor="nw")

        category10 = Button(MainCircle.canvasM, font=deFont, text="Finance", fg="#acacb7", bg="Grey", relief="groove", command= lambda: self.generateSide(5, "fi"))
        category10.pack(padx=0, pady=0)
        MainCircle.canvasM.create_window(120, 90, window=category10, anchor="nw")

        # generate the images
        for i in range(len(sliceList)):
            # define the slice image name
            directory = sliceList[i].sliceImage + sliceList[i].sliceRating + ".png"
            # define the directory itself
            img_path = os.path.join(self.current_dir, directory)
            # define the actual image itself
            sprite = ImageTk.PhotoImage(file=img_path)
            # shrink the images so that they fit on the raspberry pi
            sprite = sprite._PhotoImage__photo.subsample(3)
            # save the images to a list so that they can all display at the same time
            self.spriteLibrary.append(sprite)
            MainCircle.canvasM.image = sprite
            # place the images down, set up to be arranged in a circle, utilizing a function to decide the coordinates based on the current image (The math is so out of wack that it required a specific order in order to work properly)
            MainCircle.canvasM.create_image(((60 * math.cos(math.radians(36*i))) + (60 * math.sin(math.radians(36*i)))) + 200,\
            ((60 * math.sin(math.radians(36*i))) - (60 * math.cos(math.radians(-36*i)))) + 110,image=self.spriteLibrary[i + val], anchor="nw")
            frameM.pack(side="left")

    # generate the main circle
    def generateMain(self):
        self.createSlicesM()
        self.createCircle(0)

    # swap to the second circle
    def generateSide(self, size, category):
        frameM.pack_forget()
        SideCircleR.createSlices1(self, size, category)



# create the side circle
class SideCircleR():
    def __init__(self, the_window):
        global frame2, categories, averages
        frame2 = Frame(width=700, height=420, borderwidth=0, highlightthickness=0)
        # this sets the font for the subcategory labels
        self.fonty = font.Font(family="Palatino_Linotype", size=8, underline=1)
        # this will be the dictionary for all the category ratings
        categories = {}
        # create a list that will save all the images to be displayed
        self.spritelibrary2 = []
        # generate the dictionary for the averages of each rating
        averages = {str(x+1): 0 for x in range(10)}
        # find the directory for the images (THIS IS SO THAT THIS PROGRAM CAN BE RAN ON NOTEPAD++)
        self.current_dir = pathlib.Path(__file__).parent.resolve()
        # generate the dictionaries and lists for the coordinates of each sprite sheet image to be cropped
        self.coordinates5X = {}
        self.coordinates5Y = [0, 57, 151, 276, 438, 632, 869, 1144, 1456, 1818, 2200]
        self.coordinates6X = {}
        self.coordinates6Y = [0, 83, 195, 346, 535, 761, 1030, 1344, 1707, 2121, 2603]
        self.coordinates7X = {}
        self.coordinates7Y = [0, 78, 171, 285, 446, 637, 859, 1117, 1422, 1791, 2244]
        # get a dictionary for the subcategory names to be displayed
        self.subcategories = {}
        # create a dictionary for each category and its respective color
        self.colors = {"r": "#cb0000", "m": "#fde838", "fit": "#5bf765", "c": "#45baff", "free": "#1221ff", "k": "#7b16ff", "fri": "#f730ed", "sc": "#ff1755", "fa": "#ff6287", "fi": "#acacb7"}

    # set each rating to its corresponding category
    def rateList(self, size, prevRatings, buttonNum, sliceGroup, category):
        # reset the rating comparison
        rat = 0
        # count the amount of "high" values (count the rating) for the specific group
        for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10) + 1)):
            rat += categories[("category" + category)][str(i)]
        # set the values for each piece of each subcategory slice to either "low" (0) or "high" (1) based on its respective rating 
        if (buttonNum > rat):
            for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10) - (9 - (buttonNum)))):
                categories[("category" + category)][str(i)] = 1
        elif (buttonNum < rat):
            for i in range((buttonNum + ((int(sliceGroup) - 1) * 10)) + 1, (int(sliceGroup) * 10) + 1):
                categories[("category" + category)][str(1)] = 1
                categories[("category" + category)][str(i)] = 0
        elif (buttonNum == (rat)):
            for i in range(((int(sliceGroup) * 10) - 9), ((int(sliceGroup) * 10))):
                categories[("category" + category)][str(i)] = 0
        # clear the canvas and recreate it so the images can update (THIS IS THE REASON WHY IT IS SO SLOW, TKINTER HAS NO PROPER WIDGET REFRESH)
        SideCircleR.canvas1.destroy()
        SideCircleR.createSlices1(self, size, category)

    def Spritecoordinates(self):
        # generate the list values for each X value needed for cropping in the sprite sheets
        self.coordinates5X["1"] = [0, 45, 97, 149, 201, 253]
        self.coordinates5X["2"] = [0, 68, 158, 234, 317, 400]
        self.coordinates5X["3"] = [0, 92, 207, 322, 437, 552]
        self.coordinates5X["4"] = [0, 120, 272, 424, 576, 728]
        self.coordinates5X["5"] = [0, 144, 328, 512, 696, 880]
        self.coordinates5X["6"] = [0, 176, 403, 630, 857, 1084]
        self.coordinates5X["7"] = [0, 205, 470, 735, 1000, 1265]
        self.coordinates5X["8"] = [0, 233, 535, 837, 1139, 1441]
        self.coordinates5X["9"] = [0, 260, 598, 936, 1274, 1612]
        self.coordinates5X["10"] = [0, 294, 678, 1062, 1446, 1830]

        self.coordinates6X["1"] = [0, 59, 142, 225, 284, 367, 450]
        self.coordinates6X["2"] = [0, 80, 192, 304, 384, 496, 608]
        self.coordinates6X["3"] = [0, 109, 260, 411, 520, 671, 822]
        self.coordinates6X["4"] = [0, 137, 326, 515, 652, 841, 1030]
        self.coordinates6X["5"] = [0, 164, 390, 616, 780, 1006, 1232]
        self.coordinates6X["6"] = [0, 195, 464, 733, 928, 1197, 1466]
        self.coordinates6X["7"] = [0, 228, 542, 856, 1084, 1398, 1712]
        self.coordinates6X["8"] = [0, 265, 628, 991, 1256, 1619, 1982]
        self.coordinates6X["9"] = [0, 302, 716, 1130, 1432, 1846, 2260]
        self.coordinates6X["10"] = [0, 352, 834, 1316, 1668, 2150, 2632]

        self.coordinates7X["1"] = [0, 54, 132, 198, 272, 346, 412, 490]
        self.coordinates7X["2"] = [0, 65, 158, 237, 326, 415, 494, 587]
        self.coordinates7X["3"] = [0, 80, 194, 290, 398, 506, 604, 718]
        self.coordinates7X["4"] = [0, 113, 274, 411, 564, 717, 854, 1015]
        self.coordinates7X["5"] = [0, 135, 326, 489, 672, 853, 1016, 1207]
        self.coordinates7X["6"] = [0, 156, 378, 566, 776, 986, 1176, 1396]
        self.coordinates7X["7"] = [0, 186, 445, 659, 930, 1150, 1368, 1626]
        self.coordinates7X["8"] = [0, 215, 520, 777, 1066, 1353, 1612, 1915]
        self.coordinates7X["9"] = [0, 261, 630, 941, 1292, 1641, 1956, 2325]
        self.coordinates7X["10"] = [0, 321, 774, 1157, 1588, 2017, 2404, 2857]

        # generate the subcategory lists for each category to be displayed in the respective Side Circle
        self.subcategories["r"] = ["Relationship Quality", "Trust", "Overall Love", "Meeting People (If Single)", "General"]
        self.subcategories["m"] = ["Happiness", "Satisfaction", "Outlook on Life", "Self-Development", "General", "Decision \nMaking"]
        self.subcategories["fit"] = ["Exercise", "Diet Quality", "Wellness", "Activity", "General \nPhysical Health"]
        self.subcategories["c"] = ["Goals", "Plan for Success", "Amount of Strive", "Amount of Focus", "Satisfaction", "Productivity"]
        self.subcategories["free"] = ["Enjoyability", "Hobbies", "Healthy Separation", "Responsiblity", "Amount"]
        self.subcategories["k"] = ["Charitability", "Kindness", "Helpfulness", "Positivity", "Humility", "General \nMorality"]
        self.subcategories["fri"] = ["Friendship Quality", "Time Spent \nTogether", "Reliability", "Sociability", "Enjoyment", "Loyalty", "General"]
        self.subcategories["sc"] = ["Spirituality", "Environmental \nCleanliness", "Bodily Care", "Healthy Sleeping\n Habits", "General \nSelf-Care"]
        self.subcategories["fa"] = ["Connection Between \nMembers", "Overall Love", "Amount of Time Spent", "Thankfulness", "General"]
        self.subcategories["fi"] = ["Budgeting", "Bills and Debts Paid", "Income", "Spending Habits", "General \nFinancial Fluency"]

    def ratingListSetup(self):
        # generate the default values for the subcategories while generating the dictionary
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
        categoriez = ["r", "m", "fit", "c", "free", "k", "fri", "sc", "fa", "fi"]
        for j in range(1, 11):
            averages[str(j)] = 0
            for i in range(1, (len(categories[("category" + categoriez[j-1])]) + 1)):
                averages[str(j)] += categories[("category" + categoriez[j-1])][str(i)]
            averages[str(j)] /= (len(categories[("category" + categoriez[j-1])])/10)
        create.returning()

    # calculate the current rating compared to the previous and color the subcategory slice accordingly
    def imagename(self, size, segment, PrevRat, currentRating, group, category):
        setting = ""
        summation = 0
        for i in range(((group * 10) - 9), ((group * 10) + 1)):
            if (categories[("category" + category)][str(i)] == 1):
                summation += 1
            else:
                summation += 0
        # find out what the current rating is compared to the previous and declare what category it is supposed to be
        if (PrevRat == 1) and (currentRating == summation):
            setting = category
        elif (PrevRat == 0) and (summation > currentRating):
            setting = category
        elif (PrevRat == 1) and (summation < currentRating):
            setting = 0
        elif (PrevRat == 1) and (summation > currentRating):
            setting = category
        else:
            setting = 0


        # Get the image size of the needed button slice from the respective sprite sheet based on the set values above
        if (size == 5):
            left = self.coordinates5X[str(segment)][group - 1]
            up = self.coordinates5Y[(segment - 1)]
            right = self.coordinates5X[str(segment)][group]
            down = self.coordinates5Y[segment]
        elif (size == 6):
            left = self.coordinates6X[str(segment)][group - 1]
            up = self.coordinates6Y[(segment - 1)]
            right = self.coordinates6X[str(segment)][group]
            down = self.coordinates6Y[segment]
        elif (size == 7):
            left = self.coordinates7X[str(segment)][group - 1]
            up = self.coordinates7Y[(segment - 1)]
            right = self.coordinates7X[str(segment)][group]
            down = self.coordinates7Y[segment]


        # create the directory for the sprite sheet, define it, crop it down to the respective slice piece, resize it, filter it to make it clearer, and return the image needed
        directory = "spritesheet{}_{}.png".format(size, setting)
        img_path = os.path.join(self.current_dir, directory)
        sheet = PIL.Image.open(img_path)
        slicePiece = sheet.crop([left, up, right, down])
        w = (right - left) / 9
        h = (down - up) / 9
        slicePiece = slicePiece.resize((int(w), int(h)), resample=PIL.Image.HAMMING)
        sprite = ImageTk.PhotoImage(slicePiece)
        self.spritelibrary2.append(sprite)
        SideCircleR.canvas1.image = sprite
        return self.spritelibrary2[len(self.spritelibrary2) - 1]


    # create the slices similar to the main circle
    def createSlices1(self, size, category):
        frame2.pack(side="left")
        # define the degrees needed to rotate based on the size of the category
        division = (360 / size)

        # create the canvas
        SideCircleR.canvas1 = Canvas(frame2, width=700, height=420, bg="white")
        SideCircleR.canvas1.pack()

        def XCoordinateTime(size, group, division, segment):
            if ((group > 3) and (size <= 6)) or ((group > 4) and (size ==7)):
                addition = -10
            else:
                addition = 10
            # set an origin in the middle of the canvas
            originX = 300
            originY = 205
            # set a beginning point (the point for the first piece generated)
            pointX = 420 + ((12 * (segment-10))) 
            pointY = 35 - (18 * (segment-10)) 

            # rotate the x coordinate based on the values above
            XCoordinate = originX + math.cos(math.radians(division*(group-1))) * (pointX - originX) - math.sin(math.radians(division*(group-1))) * (pointY - originY) + addition

            return XCoordinate

        def YCoordinateTime(size, group, division, segment):
            # set an origin in the middle of the canvas
            originX = 300
            originY = 205
            # set a beginning point (the point for the first piece generated)
            pointX = 420 + ((12 * (segment-10))) 
            pointY = 35 - (18 * (segment-10)) 

            # rotate the Y coordinate based on the values above
            YCoordinate = originY + math.sin(math.radians(division*(group-1))) * (pointX - originX) + math.cos(math.radians(division*(group-1))) * (pointY - originY) -30

            return YCoordinate

        # set up the buttons for the first slice
        Button1_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(10)], 10, 1, category), relief="flat", bg="White", border = "0", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "1", category))
        Button1_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 10), YCoordinateTime(size, 1, division, 10), window=Button1_j, anchor="nw")


        # create the label for the subcategory
        Subcat1 = Label(SideCircleR.canvas1, text=create3.subcategories[category][0], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
        Subcat1.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 10) + 50, YCoordinateTime(size, 1, division, 10) + 15, window=Subcat1, anchor="nw")


        Button1_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(9)], 9, 1, category), relief="flat", bg="White", border = "0", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "1", category))
        Button1_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 9), YCoordinateTime(size, 1, division, 9), window=Button1_i, anchor="nw")

        Button1_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(8)], 8, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "1", category))
        Button1_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 8), YCoordinateTime(size, 1, division, 8), window=Button1_h, anchor="nw")

        Button1_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(7)], 7, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "1", category))
        Button1_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 7), YCoordinateTime(size, 1, division, 7), window=Button1_g, anchor="nw")

        Button1_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(6)], 6, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "1", category))
        Button1_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 6), YCoordinateTime(size, 1, division, 6), window=Button1_f, anchor="nw")

        Button1_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(5)], 5, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "1", category))
        Button1_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 5), YCoordinateTime(size, 1, division, 5), window=Button1_e, anchor="nw")

        Button1_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(4)], 4, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "1", category))
        Button1_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 4), YCoordinateTime(size, 1, division, 4), window=Button1_d, anchor="nw")

        Button1_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(3)], 3, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "1", category))
        Button1_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 3), YCoordinateTime(size, 1, division, 3), window=Button1_c, anchor="nw")

        Button1_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(2)], 2, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "1", category))
        Button1_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 2), YCoordinateTime(size, 1, division, 2), window=Button1_b, anchor="nw")

        Button1_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(1)], 1, 1, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "1", category))
        Button1_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 1, division, 1), YCoordinateTime(size, 1, division, 1), window=Button1_a, anchor="nw")





        # set up the buttons for the second slice
        Button2_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(20)], 10, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "2", category))
        Button2_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 10) + 5, YCoordinateTime(size, 2, division, 10), window=Button2_j, anchor="nw")


        # create the label for the subcategory
        Subcat2 = Label(SideCircleR.canvas1, text=create3.subcategories[category][1], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
        Subcat2.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 10) - 15, YCoordinateTime(size, 2, division, 10) + 80, window=Subcat2, anchor="nw")


        Button2_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(19)], 9, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "2", category))
        Button2_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 9), YCoordinateTime(size, 2, division, 9), window=Button2_i, anchor="nw")

        Button2_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(18)], 8, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "2", category))
        Button2_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 8), YCoordinateTime(size, 2, division, 8), window=Button2_h, anchor="nw")

        Button2_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(17)], 7, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "2", category))
        Button2_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 7), YCoordinateTime(size, 2, division, 7), window=Button2_g, anchor="nw")

        Button2_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(16)], 6, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "2", category))
        Button2_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 6), YCoordinateTime(size, 2, division, 6), window=Button2_f, anchor="nw")

        Button2_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(15)], 5, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "2", category))
        Button2_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 5), YCoordinateTime(size, 2, division, 5), window=Button2_e, anchor="nw")

        Button2_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(14)], 4, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "2", category))
        Button2_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 4), YCoordinateTime(size, 2, division, 4), window=Button2_d, anchor="nw")

        Button2_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(13)], 3, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "2", category))
        Button2_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 3), YCoordinateTime(size, 2, division, 3), window=Button2_c, anchor="nw")

        Button2_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(12)], 2, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "2", category))
        Button2_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 2), YCoordinateTime(size, 2, division, 2), window=Button2_b, anchor="nw")

        Button2_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(11)], 1, 2, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "2", category))
        Button2_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 2, division, 1), YCoordinateTime(size, 2, division, 1), window=Button2_a, anchor="nw")




        # set up the buttons for the third slice
        Button3_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(30)], 10, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "3", category))
        Button3_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 10), YCoordinateTime(size, 3, division, 10), window=Button3_j, anchor="nw")


        # create the label for the subcategory
        Subcat3 = Label(SideCircleR.canvas1, text=create3.subcategories[category][2], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
        Subcat3.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 10) + 60, YCoordinateTime(size, 3, division, 10) - 10, window=Subcat3, anchor="nw")


        Button3_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(29)], 9, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "3", category))
        Button3_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 9), YCoordinateTime(size, 3, division, 9), window=Button3_i, anchor="nw")

        Button3_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(28)], 8, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "3", category))
        Button3_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 8), YCoordinateTime(size, 3, division, 8), window=Button3_h, anchor="nw")

        Button3_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(27)], 7, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "3", category))
        Button3_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 7), YCoordinateTime(size, 3, division, 7), window=Button3_g, anchor="nw")

        Button3_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(26)], 6, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "3", category))
        Button3_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 6), YCoordinateTime(size, 3, division, 6), window=Button3_f, anchor="nw")

        Button3_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(25)], 5, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "3", category))
        Button3_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 5), YCoordinateTime(size, 3, division, 5), window=Button3_e, anchor="nw")

        Button3_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(24)], 4, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "3", category))
        Button3_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 4), YCoordinateTime(size, 3, division, 4), window=Button3_d, anchor="nw")

        Button3_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(23)], 3, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "3", category))
        Button3_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 3), YCoordinateTime(size, 3, division, 3), window=Button3_c, anchor="nw")

        Button3_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(22)], 2, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "3", category))
        Button3_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 2), YCoordinateTime(size, 3, division, 2), window=Button3_b, anchor="nw")

        Button3_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(21)], 1, 3, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "3", category))
        Button3_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 3, division, 1), YCoordinateTime(size, 3, division, 1), window=Button3_a, anchor="nw")




        # set up the buttons for the fourth slice
        Button4_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(40)], 10, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "4", category))
        Button4_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 10), YCoordinateTime(size, 4, division, 10), window=Button4_j, anchor="nw")


        # create the label for the subcategory
        Subcat4 = Label(SideCircleR.canvas1, text=create3.subcategories[category][3], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
        Subcat4.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 10) - 80, YCoordinateTime(size, 4, division, 10) - 40, window=Subcat4, anchor="nw")


        Button4_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(39)], 9, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "4", category))
        Button4_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 9), YCoordinateTime(size, 4, division, 9), window=Button4_i, anchor="nw")

        Button4_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(38)], 8, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "4", category))
        Button4_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 8), YCoordinateTime(size, 4, division, 8), window=Button4_h, anchor="nw")

        Button4_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(37)], 7, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "4", category))
        Button4_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 7), YCoordinateTime(size, 4, division, 7), window=Button4_g, anchor="nw")

        Button4_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(36)], 6, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "4", category))
        Button4_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 6), YCoordinateTime(size, 4, division, 6), window=Button4_f, anchor="nw")

        Button4_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(35)], 5, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "4", category))
        Button4_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 5), YCoordinateTime(size, 4, division, 5), window=Button4_e, anchor="nw")

        Button4_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(34)], 4, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "4", category))
        Button4_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 4), YCoordinateTime(size, 4, division, 4), window=Button4_d, anchor="nw")

        Button4_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(33)], 3, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "4", category))
        Button4_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 3), YCoordinateTime(size, 4, division, 3), window=Button4_c, anchor="nw")

        Button4_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(32)], 2, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "4", category))
        Button4_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 2), YCoordinateTime(size, 4, division, 2), window=Button4_b, anchor="nw")

        Button4_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(31)], 1, 4, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "4", category))
        Button4_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 4, division, 1), YCoordinateTime(size, 4, division, 1), window=Button4_a, anchor="nw")



        # set up the buttons for the fifth slice
        Button5_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(50)], 10, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "5", category))
        Button5_j.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 10), YCoordinateTime(size, 5, division, 10), window=Button5_j, anchor="nw")


        # create the label for the subcategory
        Subcat5 = Label(SideCircleR.canvas1, text=create3.subcategories[category][4], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
        Subcat5.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 10) - 85, YCoordinateTime(size, 5, division, 10) + 45, window=Subcat5, anchor="nw")


        Button5_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(49)], 9, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "5", category))
        Button5_i.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 9), YCoordinateTime(size, 5, division, 9), window=Button5_i, anchor="nw")

        Button5_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(48)], 8, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "5", category))
        Button5_h.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 8), YCoordinateTime(size, 5, division, 8), window=Button5_h, anchor="nw")

        Button5_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(47)], 7, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "5", category))
        Button5_g.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 7), YCoordinateTime(size, 5, division, 7), window=Button5_g, anchor="nw")

        Button5_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(46)], 6, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "5", category))
        Button5_f.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 6), YCoordinateTime(size, 5, division, 6), window=Button5_f, anchor="nw")

        Button5_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(45)], 5, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "5", category))
        Button5_e.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 5), YCoordinateTime(size, 5, division, 5), window=Button5_e, anchor="nw")

        Button5_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(44)], 4, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "5", category))
        Button5_d.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 4), YCoordinateTime(size, 5, division, 4), window=Button5_d, anchor="nw")

        Button5_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(43)], 3, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "5", category))
        Button5_c.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 3), YCoordinateTime(size, 5, division, 3), window=Button5_c, anchor="nw")

        Button5_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(42)], 2, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "5", category))
        Button5_b.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 2), YCoordinateTime(size, 5, division, 2), window=Button5_b, anchor="nw")

        Button5_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(41)], 1, 5, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "5", category))
        Button5_a.pack(padx=0, pady=0)
        SideCircleR.canvas1.create_window(XCoordinateTime(size, 5, division, 1), YCoordinateTime(size, 5, division, 1), window=Button5_a, anchor="nw")


        if (size == 6):
            # set up the buttons for the sixth slice (only if the actual category size is 6 so that the labels & buttons fit better)
            Button6_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(60)], 10, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "6", category))
            Button6_j.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 10), YCoordinateTime(size, 6, division, 10), window=Button6_j, anchor="nw")


            # create the label for the subcategory
            Subcat6 = Label(SideCircleR.canvas1, text=create3.subcategories[category][5], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
            Subcat6.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 10) - 70, YCoordinateTime(size, 6, division, 10) + 35, window=Subcat6, anchor="nw")


            Button6_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(59)], 9, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "6", category))
            Button6_i.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 9), YCoordinateTime(size, 6, division, 9), window=Button6_i, anchor="nw")

            Button6_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(58)], 8, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "6", category))
            Button6_h.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 8), YCoordinateTime(size, 6, division, 8), window=Button6_h, anchor="nw")

            Button6_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(57)], 7, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "6", category))
            Button6_g.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 7), YCoordinateTime(size, 6, division, 7), window=Button6_g, anchor="nw")

            Button6_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(56)], 6, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "6", category))
            Button6_f.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 6), YCoordinateTime(size, 6, division, 6), window=Button6_f, anchor="nw")

            Button6_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(55)], 5, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "6", category))
            Button6_e.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 5), YCoordinateTime(size, 6, division, 5), window=Button6_e, anchor="nw")

            Button6_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(54)], 4, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "6", category))
            Button6_d.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 4), YCoordinateTime(size, 6, division, 4), window=Button6_d, anchor="nw")

            Button6_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(53)], 3, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "6", category))
            Button6_c.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 3), YCoordinateTime(size, 6, division, 3), window=Button6_c, anchor="nw")

            Button6_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(52)], 2, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "6", category))
            Button6_b.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 2), YCoordinateTime(size, 6, division, 2), window=Button6_b, anchor="nw")

            Button6_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(51)], 1, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "6", category))
            Button6_a.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 1), YCoordinateTime(size, 6, division, 1), window=Button6_a, anchor="nw")



        elif (size == 7):
            # set up the buttons for the sixth slice if the category's size is 7
            Button6_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(60)], 10, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "6", category))
            Button6_j.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 10), YCoordinateTime(size, 6, division, 10), window=Button6_j, anchor="nw")


            # create the label for the subcategory
            Subcat6 = Label(SideCircleR.canvas1, text=create3.subcategories[category][5], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
            Subcat6.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 10) + 18, YCoordinateTime(size, 6, division, 10) - 40, window=Subcat6, anchor="nw")


            Button6_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(59)], 9, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "6", category))
            Button6_i.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 9), YCoordinateTime(size, 6, division, 9), window=Button6_i, anchor="nw")

            Button6_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(58)], 8, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "6", category))
            Button6_h.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 8), YCoordinateTime(size, 6, division, 8), window=Button6_h, anchor="nw")

            Button6_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(57)], 7, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "6", category))
            Button6_g.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 7), YCoordinateTime(size, 6, division, 7), window=Button6_g, anchor="nw")

            Button6_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(56)], 6, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "6", category))
            Button6_f.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 6), YCoordinateTime(size, 6, division, 6), window=Button6_f, anchor="nw")

            Button6_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(55)], 5, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "6", category))
            Button6_e.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 5), YCoordinateTime(size, 6, division, 5), window=Button6_e, anchor="nw")

            Button6_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(54)], 4, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "6", category))
            Button6_d.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 4), YCoordinateTime(size, 6, division, 4), window=Button6_d, anchor="nw")

            Button6_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(53)], 3, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "6", category))
            Button6_c.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 3), YCoordinateTime(size, 6, division, 3), window=Button6_c, anchor="nw")

            Button6_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(52)], 2, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "6", category))
            Button6_b.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 2), YCoordinateTime(size, 6, division, 2), window=Button6_b, anchor="nw")

            Button6_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(51)], 1, 6, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "6", category))
            Button6_a.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 6, division, 1), YCoordinateTime(size, 6, division, 1), window=Button6_a, anchor="nw")




            # set up the buttons for the seventh slice
            Button7_j = Button(SideCircleR.canvas1, image=create3.imagename(size, 10, categories[("category" + category)][str(70)], 10, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 10, "7", category))
            Button7_j.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 10) - 5, YCoordinateTime(size, 7, division, 10) + 15, window=Button7_j, anchor="nw")


            # create the label for the subcategory
            Subcat7 = Label(SideCircleR.canvas1, text=create3.subcategories[category][6], relief="ridge", font=create3.fonty, fg=create3.colors[category], bg="Grey")
            Subcat7.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 10) + 80, YCoordinateTime(size, 7, division, 10) + 40, window=Subcat7, anchor="nw")


            Button7_i = Button(SideCircleR.canvas1, image=create3.imagename(size, 9, categories[("category" + category)][str(69)], 9, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 9, "7", category))
            Button7_i.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 9) + 10, YCoordinateTime(size, 7, division, 9) + 20, window=Button7_i, anchor="nw")

            Button7_h = Button(SideCircleR.canvas1, image=create3.imagename(size, 8, categories[("category" + category)][str(68)], 8, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 8, "7", category))
            Button7_h.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 8) + 20, YCoordinateTime(size, 7, division, 8) + 20, window=Button7_h, anchor="nw")

            Button7_g = Button(SideCircleR.canvas1, image=create3.imagename(size, 7, categories[("category" + category)][str(67)], 7, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 7, "7", category))
            Button7_g.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 7) + 20, YCoordinateTime(size, 7, division, 7) + 20, window=Button7_g, anchor="nw")

            Button7_f = Button(SideCircleR.canvas1, image=create3.imagename(size, 6, categories[("category" + category)][str(66)], 6, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 6, "7", category))
            Button7_f.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 6) + 20, YCoordinateTime(size, 7, division, 6) + 20, window=Button7_f, anchor="nw")

            Button7_e = Button(SideCircleR.canvas1, image=create3.imagename(size, 5, categories[("category" + category)][str(65)], 5, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 5, "7", category))
            Button7_e.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 5) + 20, YCoordinateTime(size, 7, division, 5) + 20, window=Button7_e, anchor="nw")

            Button7_d = Button(SideCircleR.canvas1, image=create3.imagename(size, 4, categories[("category" + category)][str(64)], 4, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 4, "7", category))
            Button7_d.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 4) + 20, YCoordinateTime(size, 7, division, 4) + 20, window=Button7_d, anchor="nw")

            Button7_c = Button(SideCircleR.canvas1, image=create3.imagename(size, 3, categories[("category" + category)][str(63)], 3, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 3, "7", category))
            Button7_c.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 3) + 20, YCoordinateTime(size, 7, division, 3) + 20, window=Button7_c, anchor="nw")

            Button7_b = Button(SideCircleR.canvas1, image=create3.imagename(size, 2, categories[("category" + category)][str(62)], 2, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 2, "7", category))
            Button7_b.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 2) + 15, YCoordinateTime(size, 7, division, 2) + 12, window=Button7_b, anchor="nw")

            Button7_a = Button(SideCircleR.canvas1, image=create3.imagename(size, 1, categories[("category" + category)][str(61)], 1, 7, category), relief="flat", bg="White", command= lambda: create3.rateList(size, categories[("category" + category)], 1, "7", category))
            Button7_a.pack(padx=0, pady=0)
            SideCircleR.canvas1.create_window(XCoordinateTime(size, 7, division, 1) + 13, YCoordinateTime(size, 7, division, 1) + 5, window=Button7_a, anchor="nw")




        # generate the back button that returns the user to the main circle
        backButton = Button(SideCircleR.canvas1, font=deFont, text="Back", relief="raised", fg="Black", command= lambda: create3.goBackToMain(categories[("category" + category)], frame2))
        backButton.pack()
        SideCircleR.canvas1.create_window(20, 20, window=backButton, anchor="nw")


# create the text frame :]
class TextFrame():
    def __init__(self, the_window):
        # generate the text frame
        frame2 = Frame(width=100, height=420, bg="grey")
        frame2.pack(side="right")
        # generate the text frame's canvas
        canvas2 = Canvas(frame2, width=200, height=410, bg="grey")
        # create the font for the button
        textfont = font.Font(family="Palatino_Linotype", weight="bold", size=15, underline=1) 
        canvas2.pack()
        # create the button that opens the resources tab
        button = Button(canvas2, text = "Resources", font=textfont, bg = "grey", height = 30, width = 10, command = self.open_list)
        button.pack()
        # get the image paths
        self.current_dir = pathlib.Path(__file__).parent.resolve()

    # open the script that contains the resources code 
    # we decided to import it as a separate script because it's like 1500 lines of code, we got sick of trying to make stuff dynamic
    # since it took waaayyyy too much time for a result that might require the complete restructuring of code
    def open_list(self):
        # define the directory
        directory = "QRCodes.py"
        py_path = os.path.join(self.current_dir, directory)
        # open the resources script to be used
        exec(open(py_path).read())
        # generate the resources window
        createSourcesWindow()
        


###################################################################
# Main Program
###################################################################

# set the window size to what the Raspberry Pi's dimensions are
width = 800
height = 420

# generate the GUI window
window = Tk()
window.geometry("{}x{}".format(width, height))
window.title("Level 10 Life")

# generate the frames and all that crap
create = MainCircle(window)
create2 = TextFrame(window)
create3 = SideCircleR(window)
# define the lists needed at all times
create3.ratingListSetup()
create3.Spritecoordinates()
# start the show!
create.generateMain()

window.mainloop
