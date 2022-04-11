#resources list... buttons leading to buttons leading to QR codes

#library
from tkinter import *


# Create the root window [categories]
root = Tk()
root.title("Categories")
root.geometry("300x470")

# Create label for root window [categories]
label1 = Label(root, text = "This is the categories window")

####################################################################THE QR CODES FOR KARMA
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


####################################################################THE QR CODES FOR FRIENDS
#spending time top level window
# window which is not associated with any parent window
def spending_friend():    
    
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
    photo = PhotoImage(file="time_friends.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#reliable top level window
# window which is not associated with any parent window
def reliable():    
    
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
    photo = PhotoImage(file="reliable.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#social top level window
# window which is not associated with any parent window
def social():    
    
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
    photo = PhotoImage(file="social.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#fun top level window
# window which is not associated with any parent window
def fun():    

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
    photo = PhotoImage(file="fun.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#loyal top level window
# window which is not associated with any parent window
def loyal():    
    
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
    photo = PhotoImage(file="loyalty.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#wholesome (good) top level window
# window which is not associated with any parent window
def good():    
    
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
    photo = PhotoImage(file="good_friend.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#friends_general top level window
# window which is not associated with any parent window
def friends_general():    
    
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
    photo = PhotoImage(file="Friends.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR FAMILY

#thankfulness top level window
# window which is not associated with any parent window
def thankfulness():    
    
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
    photo = PhotoImage(file="thankfulness.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#spending time with family level window
# window which is not associated with any parent window
def spending_family():    

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
    photo = PhotoImage(file="time_family.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#loving top level window
# window which is not associated with any parent window
def loving():    
    
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
    photo = PhotoImage(file="loving.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#connected top level window
# window which is not associated with any parent window
def connected():    
    
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
    photo = PhotoImage(file="connected.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#family_general top level window
# window which is not associated with any parent window
def family_general():    
    
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
    photo = PhotoImage(file="Family.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()


#############################################################################THE QR CODES FOR FINANCE

#spending responsibly top level window
# window which is not associated with any parent window
def spending():    
    
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
    photo = PhotoImage(file="spending.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#good income time with family level window
# window which is not associated with any parent window
def income():    

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
    photo = PhotoImage(file="income.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#bills getting paid top level window
# window which is not associated with any parent window
def bills():    
    
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
    photo = PhotoImage(file="bills.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#budgeting top level window
# window which is not associated with any parent window
def budget():    
    
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
    photo = PhotoImage(file="budget.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#finance_general top level window
# window which is not associated with any parent window
def finance_general():    
    
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
    photo = PhotoImage(file="Finance.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR FAMILY

#thankfulness top level window
# window which is not associated with any parent window
def thankfulness():    
    
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
    photo = PhotoImage(file="thankfulness.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#spending time with family level window
# window which is not associated with any parent window
def spending_family():    

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
    photo = PhotoImage(file="time_family.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#loving top level window
# window which is not associated with any parent window
def loving():    
    
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
    photo = PhotoImage(file="loving.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#connected top level window
# window which is not associated with any parent window
def connected():    
    
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
    photo = PhotoImage(file="connected.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#family_general top level window
# window which is not associated with any parent window
def family_general():    
    
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
    photo = PhotoImage(file="Family.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR CAREER

#goals top level window
# window which is not associated with any parent window
def goals():    
    
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
    photo = PhotoImage(file="goals.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#success plan level window
# window which is not associated with any parent window
def plan():    

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
    photo = PhotoImage(file="success.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#strive  level window
# window which is not associated with any parent window
def strive():    

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
    photo = PhotoImage(file="strive.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#on track top level window
# window which is not associated with any parent window
def track():    
    
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
    photo = PhotoImage(file="track.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#productive top level window
# window which is not associated with any parent window
def productive():    
    
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
    photo = PhotoImage(file="productive.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#career_general top level window
# window which is not associated with any parent window
def career_general():    
    
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
    photo = PhotoImage(file="Career.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()


#############################################################################THE QR CODES FOR FREETIME

#enjoyable level window
# window which is not associated with any parent window
def enjoyable():    

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
    photo = PhotoImage(file="enjoyable.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#hobbies  level window
# window which is not associated with any parent window
def hobbies():    

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
    photo = PhotoImage(file="hobbies.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#healthy top level window
# window which is not associated with any parent window
def healthy():    
    
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
    photo = PhotoImage(file="healthy_free.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#responsible top level window
# window which is not associated with any parent window
def responsible():    
    
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
    photo = PhotoImage(file="responsible.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#freetime_general top level window
# window which is not associated with any parent window
def freetime_general():    
    
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
    photo = PhotoImage(file="Freetime.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR ROMANCE

#Good relationship level window
# window which is not associated with any parent window
def good_rel():    

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
    photo = PhotoImage(file="good_rel.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#trustworthy  level window
# window which is not associated with any parent window
def trustworthy():    

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
    photo = PhotoImage(file="trust_rel.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#in love top level window
# window which is not associated with any parent window
def inlove():    
    
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
    photo = PhotoImage(file="love.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#meeting people top level window
# window which is not associated with any parent window
def meeting():    
    
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
    photo = PhotoImage(file="meeting.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#romance_general top level window
# window which is not associated with any parent window
def romance_general():    
    
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
    photo = PhotoImage(file="Romance.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()


#############################################################################THE QR CODES FOR FITNESS

#exercising level window
# window which is not associated with any parent window
def exercising():    

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
    photo = PhotoImage(file="exercise.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#eating  level window
# window which is not associated with any parent window
def eating():    

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
    photo = PhotoImage(file="eating.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#health top level window
# window which is not associated with any parent window
def health():    
    
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
    photo = PhotoImage(file="health.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#active top level window
# window which is not associated with any parent window
def active():    
    
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
    photo = PhotoImage(file="active.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#fitness_general top level window
# window which is not associated with any parent window
def fitness_general():    
    
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
    photo = PhotoImage(file="Fitness.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR SELFCARE

#clean environemnt level window
# window which is not associated with any parent window
def clean():    

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
    photo = PhotoImage(file="clean_env.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#spiritual self care  level window
# window which is not associated with any parent window
def spirit():    

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
    photo = PhotoImage(file="spiritual.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#adequate sleep top level window
# window which is not associated with any parent window
def sleep():    
    
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
    photo = PhotoImage(file="sleep.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#clean apperance top level window
# window which is not associated with any parent window
def appearance():    
    
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
    photo = PhotoImage(file="clean_app.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#selfcare_general top level window
# window which is not associated with any parent window
def selfcare_general():    
    
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
    photo = PhotoImage(file="self-care.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#############################################################################THE QR CODES FOR MINDSET

#happy level window
# window which is not associated with any parent window
def happy():    

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
    photo = PhotoImage(file="happy.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#satisfied  level window
# window which is not associated with any parent window
def satisfied():    

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
    photo = PhotoImage(file="satisfied.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()
    
#optimistic top level window
# window which is not associated with any parent window
def optimistic():    
    
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
    photo = PhotoImage(file="optimistic.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#self development top level window
# window which is not associated with any parent window
def development():    
    
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
    photo = PhotoImage(file="self_development.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()

#mindset_general top level window
# window which is not associated with any parent window
def mindset_general():    
    
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
    photo = PhotoImage(file="Mindset.gif")
    L1 = Label(top2, image=photo)

    L1.photo = photo #this prevents garbage collection from memory
    
    #packing into window
    label.pack()
    L1.pack()
    button.pack()
        
    # Display until closed manually.
    top2.mainloop()


    
##################################################################################################   
##############################################################################KARMA'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_karma():
    
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


##############################################################################FRIEND'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_friends():
    
    # Create widget
    top1 = Toplevel(root)
    
    # Define title for window
    top1.title("Subcategories")
    
    # specify size
    top1.geometry("200x250")
    
    # Create label
    label = Label(top1, text = "This is the subcategories window")
    
    # Create Exit button
    button1 = Button(top1, text = "Exit", command = top1.destroy)
    
    # create button to open QR codes for each subcatergory 
    button2 = Button(top1, text = "Spending time", command = spending_friend)
    button3 = Button(top1, text = "Reliable", command = reliable)
    button4 = Button(top1, text = "Social", command = social)
    button5 = Button(top1, text = "Fun", command = fun)
    button6 = Button(top1, text = "Loyal", command = loyal)
    button7 = Button(top1, text = "Wholesome", command = good)
    button8 = Button(top1, text = "General", command = friends_general)
    
    label.pack()
    button8.pack()
    button7.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################FAMILY'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_family():
    
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
    button2 = Button(top1, text = "Thankfulness", command = thankfulness)
    button3 = Button(top1, text = "Spending time", command = spending_family)
    button4 = Button(top1, text = "Loving", command = loving)
    button5 = Button(top1, text = "Connected", command = connected)
    button6 = Button(top1, text = "General", command = family_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################FINANCE'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_finance():
    
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
    button2 = Button(top1, text = "Spending responsibly", command = spending)
    button3 = Button(top1, text = "Good income", command = income)
    button4 = Button(top1, text = "Bills getting paid", command = bills)
    button5 = Button(top1, text = "Budgeting", command = budget)
    button6 = Button(top1, text = "General", command = finance_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()
    
    
##############################################################################CAREER'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_career():
    
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
    button2 = Button(top1, text = "Goals", command = goals)
    button3 = Button(top1, text = "Success plan", command = plan)
    button4 = Button(top1, text = "Strive", command = strive)
    button5 = Button(top1, text = "On track", command = track)
    button6 = Button(top1, text = "Productive", command = productive)
    button7 = Button(top1, text = "General", command = career_general)
    
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

 ##############################################################################FREETIME'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_freetime():
    
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
    button2 = Button(top1, text = "Enjoyable", command = enjoyable)
    button3 = Button(top1, text = "Hobbies", command = hobbies)
    button4 = Button(top1, text = "Healthy", command = healthy)
    button5 = Button(top1, text = "Responsible", command = responsible)
    button6 = Button(top1, text = "General", command = freetime_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################ROMANCE'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_romance():
    
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
    button2 = Button(top1, text = "Good relationship", command = good_rel)
    button3 = Button(top1, text = "Trustworthy", command = trustworthy)
    button4 = Button(top1, text = "In love", command = inlove)
    button5 = Button(top1, text = "Meeting people", command = meeting)
    button6 = Button(top1, text = "General", command = romance_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################FITNESS'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_fitness():
    
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
    button2 = Button(top1, text = "Exercising", command = exercising)
    button3 = Button(top1, text = "Eating healthy", command = eating)
    button4 = Button(top1, text = "Health", command = health)
    button5 = Button(top1, text = "Active", command = active)
    button6 = Button(top1, text = "General", command = fitness_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################SELFCARE'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_selfcare():
    
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
    button2 = Button(top1, text = "Clean environment", command = clean)
    button3 = Button(top1, text = "Spiritual self-care", command = spirit)
    button4 = Button(top1, text = "Adequate sleep", command = sleep)
    button5 = Button(top1, text = "Clean appearance", command = appearance)
    button6 = Button(top1, text = "General", command = selfcare_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()

##############################################################################MINDSET'S SUBCATGORIES
# define a function for 1st toplevel
# which is associated with root window.
def open_mindset():
    
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
    button2 = Button(top1, text = "Happy", command = happy)
    button3 = Button(top1, text = "Satisfied", command = satisfied)
    button4 = Button(top1, text = "Optimistic outlook", command = optimistic)
    button5 = Button(top1, text = "Self development", command = development)
    button6 = Button(top1, text = "General", command = mindset_general)
    
    label.pack()
    button6.pack()
    button5.pack()
    button4.pack()
    button3.pack()
    button2.pack()
    button1.pack()
    
    # Display until closed manually
    top1.mainloop()


###########################################################################FINISHING TOUCHES FOR MAIN [categories]
# Create buttons to open each individual category
button1 = Button(root, text = "Karma", command = open_karma)
button2 = Button(root, text = "Friends", command = open_friends)
button3 = Button(root, text = "Family", command = open_family)
button4 = Button(root, text = "Finance", command = open_finance)
button5 = Button(root, text = "Career", command = open_career)
button6 = Button(root, text = "Freetime", command = open_freetime)
button7 = Button(root, text = "Romance", command = open_romance)
button8 = Button(root, text = "Fitness", command = open_fitness)
button9 = Button(root, text = "Self-care", command = open_selfcare)
button10 = Button(root, text = "Mindset", command = open_mindset)

# Create Exit button
button11 = Button(root, text = "Exit", command = root.destroy)

label1.pack() #got this from start

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
button11.place(x = 120, y = 430)

# Display until closed manually
root.mainloop()



