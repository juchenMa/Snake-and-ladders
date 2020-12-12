from tkinter import *
from Game_page import *
from Player_Class import *


class Name_page(object):
    def __init__(self, player_number, master=None):
        self.root = master
        # Get the display size, adjust the interface position according to the display size to make it center
        w = 550
        h = 150 + player_number * 30
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.config(bg='pink')
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # Receive the number of players and define the variable name
        self.player_number = player_number
        # Define frame
        self.page = Frame(self.root, bg='pink')
        self.page.pack()
        self.player_name = []
        self.player_list = []
        # Initialize the entry list
        self.var_label1 = []
        self.label1 = None
        self.button1 = None
        self.button2 = None
        # Define the text before entry and display them in the label
        self.entry_name = []
        self.entry_name.append(Label(self.page, text="First player's name:", bg='pink'))
        self.entry_name.append(Label(self.page, text="Second player's name:", bg='pink'))
        self.entry_name.append(Label(self.page, text="Third player's name:", bg='pink'))
        self.entry_name.append(Label(self.page, text="Fourth player's name:", bg='pink'))
        # Enter the page creation function
        self.create_player()

    # page creation function
    def create_player(self):
        # define label showing 'please enter the name of players:'
        self.label1 = Label(self.page, text='Please enter the name of players:', width=75, height=3, bg='yellow')
        self.label1.grid(row=0, column=0, columnspan=5)
        # According to the number of players, change the corresponding element in the entry list to entry
        for i in range(0, self.player_number):
            self.var_label1.append(Entry(self.page, show=None))
            self.var_label1[i].grid(row=i + 1, column=2)
            self.entry_name[i].grid(row=i + 1, column=1)
        # Define the confirmation button and bind it to the start game function
        # When you click OK, the start_game function is automatically called
        self.button1 = Button(self.page, command=self.start_game, text='YES')
        self.button1.grid(row=self.player_number + 3, column=0)
        # Define exit button
        self.button2 = Button(self.page, command=self.root.quit, text='Exit')
        self.button2.grid(row=self.player_number + 3, column=4)
        self.root.mainloop()

    def start_game(self):
        # Determine whether the input name conforms to the format, it cannot be a space, the input is empty,
        # there are duplicates
        for i in range(0, self.player_number):
            # Determine whether the input is empty
            if len(self.var_label1[i].get()) == 0:
                tkinter.messagebox.showinfo(message='Sorry, Input can not be empty! Please enter again')
                self.page.destroy()
                Name_page(self.player_number, self.root)
            # Determine whether the input is a space
            elif self.var_label1[i].get().isspace():
                tkinter.messagebox.showinfo(message='Sorry, name cannot be a space! Please enter again')
                self.page.destroy()
                Name_page(self.player_number, self.root)
            # If the above two conditions are not met, add the name to the list
            else:
                self.player_name.append(self.var_label1[i].get())

        # Determine whether there are duplicates in the entered name
        dic = {}.fromkeys(self.player_name)
        if len(dic) == len(self.player_name):
            # The name is not repeated, Generate instances of the game player classes, pass them to the game interface
            self.page.destroy()
            for i in range(0, self.player_number):
                self.player_list.append(Player(self.player_name[i], 0, 0))
            Game_page(self.player_list, self.root)
        else:
            # The name is repeated, re-enter
            tkinter.messagebox.showinfo(message='Sorry, there are same names!\n Please enter again!')
            self.page.destroy()
            Name_page(self.player_number, self.root)
