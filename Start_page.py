import tkinter.messagebox
from Name_page import *


# Game start interface category, select the number of people
class Start_page(object):
    def __init__(self, master=None):
        self.root = master
        # Get the display size, adjust the interface position according to the display size to make it center
        w = 500
        h = 250
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.config(bg='pink')
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.page = None
        self.label1 = None
        self.button2 = None
        self.button1 = None
        self.var = IntVar()
        self.Radiobutton = []
        self.create()

    def create(self):
        # initialization Frame
        self.page = Frame(bg='pink')
        self.page.pack_propagate(0)
        self.page.pack()
        # initialization Label showing “Please choose number of players:”
        self.label1 = Label(self.page, text='Please choose number of players:', width=75, height=3, bg='yellow')
        self.label1.grid(row=1, column=0, columnspan=5)
        # initialization Single button
        for i in range(0, 4):
            self.Radiobutton.append(
                Radiobutton(self.page, text="%s" % str(i + 1), variable=self.var, value=i + 1).grid(
                    row=i + 2, column=2))
        # initialization Confirm button
        self.button1 = Button(self.page, command=self.get_data, text='YES')
        self.button1.grid(row=6, column=0)
        # initialization Exit button
        self.button2 = Button(self.page, command=self.root.quit, text='Exit')
        self.button2.grid(row=6, column=4)
        self.root.mainloop()

    def get_data(self):
        # The user did not choose the number of people to confirm directly
        if self.var.get() == 0:
            tkinter.messagebox.showinfo(message='Sorry! Please chose a number!')
            self.page.destroy()
            Start_page(self.root)
        # The user selects the number of people and confirms
        else:
            tkinter.messagebox.showinfo(message='There will be %d player!' % self.var.get())
        # Destroy the frame and pass root and player number to the name interface
            self.page.destroy()
            Name_page(self.var.get(), self.root)
