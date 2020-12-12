import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random
import End_page
from Player_Class import Player


class Game_page(object):
    def __init__(self, player, master=None):
        self.root = master
        # Get the display size, adjust the interface position according to the display size to make it center
        w = 700
        h = 450
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        # define root
        self.root.config(bg='pink')
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # initial Frame
        self.frame = Frame(self.root, bg='pink')
        self.canvas = None
        # initial users' information and list we are going to use in following work
        self.player_name = []
        self.player_number = len(player)
        self.computer_num = 0
        self.dice_point = []
        self.total_point = []
        # initial StringVar() list for displaying information in label and Player turn StringVar()
        self.text_information = []
        self.text_player_turn = StringVar()
        # initial label list and label and button
        self.information_label = []
        self.label_player_turn = None
        self.button_roll_dice = None
        self.button_start_game = None
        #  List of labels used to display pictures of each player's pieces
        self.pic_label = []
        # initial the variable name of the map image generated on the canvas
        self.map_image = None
        # initial the variable name list of the chess image generated on the canvas
        self.pos_image = []
        #  Dice image file list
        self.dice_image_file = []
        # Checkerboard image file
        self.map_image_file = None
        # Chess piece image file
        self.pos_image_file = []
        # initial color board list
        self.color_board_list = ['MediumSpringGreen', 'Gold', 'Plum', 'MediumSlateBlue']
        # initial the gaming index of the game
        self.now_index = 0
        # get the name from Player class list
        for i in range(0, len(player)):
            self.player_name.append(player[i].get_name())
        # enter generate_pic function
        self.generate_pic()

    def generate_pic(self):
        # Read the map picture, six dice pictures, and four chess pieces pictures, and call the resize function to
        # adjust their size
        map_image_temple = Image.open('D:/OneDrive/Documents/project/Snake and ladders/pic.gif')
        map_image_resized = resize(400, 400, map_image_temple)
        self.map_image_file = ImageTk.PhotoImage(map_image_resized)

        pos_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/chess1.gif')
        pos_image_resized = resize(30, 30, pos_image)
        self.pos_image_file.append(ImageTk.PhotoImage(pos_image_resized))

        pos_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/chess2.gif')
        pos_image_resized = resize(30, 30, pos_image)
        self.pos_image_file.append(ImageTk.PhotoImage(pos_image_resized))

        pos_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/chess3.gif')
        pos_image_resized = resize(30, 30, pos_image)
        self.pos_image_file.append(ImageTk.PhotoImage(pos_image_resized))

        pos_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/chess4.gif')
        pos_image_resized = resize(30, 30, pos_image)
        self.pos_image_file.append(ImageTk.PhotoImage(pos_image_resized))

        dice1_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice1.gif')
        dice1_image_resized = resize(50, 50, dice1_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice1_image_resized))

        dice2_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice2.gif')
        dice2_image_resized = resize(50, 50, dice2_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice2_image_resized))

        dice3_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice3.gif')
        dice3_image_resized = resize(50, 50, dice3_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice3_image_resized))

        dice4_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice4.gif')
        dice4_image_resized = resize(50, 50, dice4_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice4_image_resized))

        dice5_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice5.gif')
        dice5_image_resized = resize(50, 50, dice5_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice5_image_resized))

        dice6_image = Image.open('D:/OneDrive/Documents/project/Snake and ladders/dice6.gif')
        dice6_image_resized = resize(50, 50, dice6_image)
        self.dice_image_file.append(ImageTk.PhotoImage(dice6_image_resized))
        # enter generate root function
        self.generate_root()

    def generate_root(self):
        # generate root function
        # Determine whether the number of players is 1, if it is 1, add computer_num
        # The number of game players becomes 2
        if self.player_number == 1:
            self.player_number = 2
            self.player_name.append('computer')
            self.dice_point.append(0)
            self.total_point.append(0)
            self.text_information.append(StringVar())
            self.computer_num = 1
        # initial canvas
        self.canvas = Canvas(self.frame, bg='Tomato', height=450, width=400)
        self.canvas.grid(row=0, rowspan=self.player_number + 2, column=0, columnspan=self.player_number + 2)
        # generate canvas map image
        self.map_image = self.canvas.create_image(200, 200, image=self.map_image_file, tag='map')
        # generate label showing player's turn
        self.label_player_turn = Label(self.frame, bg='AntiqueWhite', textvariable=self.text_player_turn)
        self.label_player_turn.grid(row=0, column=self.player_number + 2)
        # Define the start game button and bind it to the start_game function. You cannot shake the dice before clicking
        self.button_start_game = Button(self.frame, text='start game', width=10, height=1, command=self.start_game)
        self.button_start_game.grid(row=self.player_number + 1, column=self.player_number + 2)
        # Define the dice sub button and bind the throw_dice function
        self.button_roll_dice = Button(self.frame, text='roll dice', width=10, height=1, command=lambda: self.
                                       rolling_dice())
        # When the start game button is not clicked, the dice button cannot be clicked
        self.button_roll_dice['state'] = "disabled"
        self.button_roll_dice.grid(row=self.player_number + 1, column=self.player_number + 3)
        self.frame.grid()
        self.text_player_turn.set(" 's chance")

        for i in range(0, self.player_number):
            # Add elements to the dice list and total point according to the number of game players
            self.dice_point.append(0)
            self.total_point.append(0)
            # add StringVar used to display the current dice points of each player and the current total score into list
            self.text_information.append(StringVar())
            self.text_information[i].set("Total point of %s is %d\n Point of '%s' is %d" % (
                self.player_name[i], 0, self.player_name[i], 0))
            # initial Label used to display the current dice points of each player and the current total score
            self.information_label.append(
                Label(self.frame, bg=self.color_board_list[i], textvariable=self.text_information[i]))
            self.information_label[i].grid(row=i + 1, column=self.player_number + 2)
            # initial List of labels used to display pictures of each player's pieces
            self.pic_label.append(Label(self.frame, bg='black', image=self.pos_image_file[i]))
            self.pic_label[i].grid(row=i + 1, column=self.player_number + 3)
            # generate canvas chess image
            self.pos_image.append(self.canvas.create_image(-20, 380, image=self.pos_image_file[i]))
        self.root.mainloop()

    # The user clicks the start game button to call the game start function
    def start_game(self):
        # Prompt the user to start the game
        tkinter.messagebox.showinfo(message='Game Start !!')
        # Disable the start game button and enable the dice button
        self.button_roll_dice['state'] = "normal"
        self.button_start_game['state'] = "disabled"

    # Every time the user clicks the dice sub button, the dice sub function is called once
    def rolling_dice(self):
        # Generate random numbers from 1 to 6
        self.dice_point[self.now_index] = random.randint(1, 6)
        # Die pictures for mobile users
        self.canvas.create_image(200, 425, image=self.dice_image_file[self.dice_point[self.now_index] - 1], tag='dice')
        # Judgment whether meet ladder and snake conditional
        if self.total_point[self.now_index] + self.dice_point[self.now_index] > 100:
            self.total_point[self.now_index] = self.total_point[self.now_index]
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 3:
            self.total_point[self.now_index] = 51
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 6:
            self.total_point[self.now_index] = 27
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 20:
            self.total_point[self.now_index] = 70
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 36:
            self.total_point[self.now_index] = 55
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 63:
            self.total_point[self.now_index] = 95
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 68:
            self.total_point[self.now_index] = 98
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 34:
            self.total_point[self.now_index] = 1
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 25:
            self.total_point[self.now_index] = 5
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 47:
            self.total_point[self.now_index] = 19
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 87:
            self.total_point[self.now_index] = 57
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 65:
            self.total_point[self.now_index] = 52
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 91:
            self.total_point[self.now_index] = 61
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 99:
            self.total_point[self.now_index] = 69
        elif self.total_point[self.now_index] + self.dice_point[self.now_index] == 100:
            # if anyone reach the destination
            # if there is no computer, end game
            if self.computer_num == 0:
                self.total_point[self.now_index] = self.total_point[self.now_index] + self.dice_point[self.now_index]
                tkinter.messagebox.showinfo(
                    message='Congratulations! "%s" have reach the destination ' % self.player_name[self.now_index])
                self.end_game(self.now_index)
                return
            # if there is one computer and the winner is player, end game
            elif self.now_index == 0:
                self.total_point[self.now_index] = self.total_point[self.now_index] + self.dice_point[self.now_index]
                tkinter.messagebox.showinfo(
                    message='Congratulations! %s have reach the destination' % self.player_name[self.now_index])
                self.end_game(self.now_index)
                return
            # if there is one computer and the winner is computer, end game
            else:
                self.total_point[self.now_index] = self.total_point[self.now_index] + self.dice_point[self.now_index]
                tkinter.messagebox.showinfo(
                    message='Sorry! The computer has reach the destination, you lost!')
                self.end_game(self.now_index)
                return
        # if no one reach the destination
        else:
            self.total_point[self.now_index] = self.total_point[self.now_index] + self.dice_point[self.now_index]
        # Update the position of the chess piece on the map, delete the previous chess piece
        self.canvas.delete(self.pos_image[self.now_index])
        self.pos_image[self.now_index] = self.canvas.create_image(calculate_pos(self.total_point[self.now_index])[0],
                                                                  calculate_pos(self.total_point[self.now_index])[1],
                                                                  image=self.pos_image_file[self.now_index])
        # Call the change turn function Move the game to the next player, change the index value of the current game
        # player
        self.change_turn(self.now_index)

    # change turn function
    def change_turn(self, index):
        # Change the player name in the player turn label
        self.text_player_turn.set("'%s' 's chance" % self.player_name[self.now_index])
        # Update the player’s points in the label
        for i in range(0, self.player_number):
            self.text_information[i].set("Total point of %s is %d\n Point of '%s' is %d" % (
                self.player_name[i], self.total_point[i], self.player_name[i], self.dice_point[i]))
        # Determine who the next player is, if next should be first player
        if index == self.player_number - 1:
            self.now_index = 0
        # else index +1
        else:
            self.now_index = self.now_index + 1

    # Destroy the current interface and transfer the game result to the result interface
    def end_game(self, winner_index):
        self.frame.destroy()
        End_page.End_page(self.total_point, self.player_name, winner_index, self.root)


# Pass in the size of the picture you want to adjust, and the picture file
def resize(w_box, h_box, pil_image1):
    w, h = pil_image1.size
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image1.resize((width, height), Image.ANTIALIAS)


# function used to calculate the position of chess pic in the canvas
def calculate_pos(point):
    x = point % 10
    y = (point - x) / 10
    post = [x * 40 - 20, 380 - y * 40]
    if x == 0:
        return [380, 420 - y * 40]
    else:
        return post
