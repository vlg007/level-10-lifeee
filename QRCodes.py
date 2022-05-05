#resources list

from tkinter import *




#Charity top level window
# window which is not associated with any parent window
def charity():    
    
    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="charity.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#kindness top level window
# window which is not associated with any parent window
def kindness():    
    
    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="kindness.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#helpfulness top level window
# window which is not associated with any parent window
def helpfulness():    
    
    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="helpfulness.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#positivity top level window
# window which is not associated with any parent window
def positivity():    

    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="positivity.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#humility top level window
# window which is not associated with any parent window
def humility():    
    
    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="humility.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#karma_general top level window
# window which is not associated with any parent window
def karma_general():    
    
    # Create widget
    top2 = Toplevel()
        
    # define title for window
    top2.title("QR codes")
        
    # specify size
    top2.geometry("400x560")
        
    # Create label
    label = Label(top2, text = "This is a QR code of a website to help you.")
        
    # Create exit button.
    button = Button(top2, text = "Exit", command = top2.destroy)

    # put image on
    photo = PhotoImage(file="Karma.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

    
# define a function for 1st toplevel
# which is associated with root window.
def open_Toplevel1():
    
    # Create widget
    top1 = Toplevel(root)
    
    # Define title for window
    top1.title("Subcategories")
    
    # specify size
    top1.geometry("200x200")
    
    # Create label
    label = Label(top1, text = "This is the subcategories window")
    
    # Create Exit button
    button1 = Button(top1, text = "Exit", command = top1.destroy)
    
    # create button to open QR codes for each subcatergory 
    button2 = Button(top1, text = "Charity", command = charity)
    button3 = Button(top1, text = "Kindness", command = kindness)
    button4 = Button(top1, text = "Helpfulness", command = helpfulness)
    button5 = Button(top1, text = "Positivity", command = positivity)
    button6 = Button(top1, text = "Humility", command = humility)
    button7 = Button(top1, text = "General", command = karma_general)
    
    label.pack()
    button7.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()


def createSourcesWindow():
    global root
    # Create the root window [categories]
    root = Tk()
    root.title("Categories")
    root.geometry("300x450")

    # Create label for root window [categories]
    label1 = Label(root, text = "This is the categories window")
    
    # Create button to open toplevel1
    button1 = Button(root, text = "Karma", command = open_Toplevel1)
    button2 = Button(root, text = "Friends", command = open_Toplevel1)
    button3 = Button(root, text = "Family", command = open_Toplevel1)
    button4 = Button(root, text = "Finance", command = open_Toplevel1)
    button5 = Button(root, text = "Career", command = open_Toplevel1)
    button6 = Button(root, text = "Freetime", command = open_Toplevel1)
    button7 = Button(root, text = "Romance", command = open_Toplevel1)
    button8 = Button(root, text = "Fitness", command = open_Toplevel1)
    button9 = Button(root, text = "Self-care", command = open_Toplevel1)
    button10 = Button(root, text = "Mindset", command = open_Toplevel1)

    label1.pack()

    # position the button
    button1.place(x = 120, y = 30)
    button2.place(x = 120, y = 70)
    button3.place(x = 120, y = 110)
    button4.place(x = 120, y = 150)
    button5.place(x = 120, y = 190)
    button6.place(x = 120, y = 230)
    button7.place(x = 120, y = 270)
    button8.place(x = 120, y = 310)
    button9.place(x = 120, y = 350)
    button10.place(x = 120, y = 390)

    # Display until closed manually
    root.mainloop()



