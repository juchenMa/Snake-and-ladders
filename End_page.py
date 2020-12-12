from tkinter import *
import Start_page


class End_page(object):
    def __init__(self, final_point, player_name, winner_index, master=None):
        self.root = master
        w = 320
        h = 90 + (len(player_name) - 2) * 20
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.config(bg='pink')
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.final_point = final_point
        self.player_name = player_name
        self.winner_index = winner_index
        self.shown_text = StringVar()
        self.frame = None
        self.label = None
        self.button1 = None
        self.button2 = None
        self.player_match_ordered = None
        self.player_match = {}

        for i in range(0, len(self.player_name)):
            self.player_match[self.player_name[i]] = self.final_point[i]
        print(self.player_match)
        self.player_match_ordered = sorted(self.player_match.items(), key=lambda x: x[1], reverse=True)

        self.create_pag()

    def create_pag(self):
        self.root.title()
        self.frame = Frame(self.root, bg='Gold')
        self.root.title('Final result')
        # show the final result  and define text we needed
        text_1 = "Winner : %s, getting point %d !\n " % (
            self.player_match_ordered[0][0], self.player_match_ordered[0][1])
        text_2 = '2nd : %s , getting point %d !\n ' % (
            self.player_match_ordered[1][0], self.player_match_ordered[1][1])

        if len(self.player_name) == 2:
            self.shown_text.set(text_1 + text_2)
        elif len(self.player_name) == 3:
            text_3 = '3rd : %s , getting point %d !\n ' % (
                self.player_match_ordered[2][0], self.player_match_ordered[2][1])
            self.shown_text.set(text_1 + text_2 + text_3)
        elif len(self.player_name) == 4:
            text_3 = '3rd : %s , getting point %d !\n ' % (
                self.player_match_ordered[2][0], self.player_match_ordered[2][1])
            text_4 = '4th : %s , getting point %d !\n' % (
                self.player_match_ordered[3][0], self.player_match_ordered[3][1])
            self.shown_text.set(text_1 + text_2 + text_3 + text_4)

        self.label = Label(self.frame, bg='Gold', textvariable=self.shown_text)
        self.label.grid(row=0, rowspan=5, column=1, columnspan=5)
        self.button1 = Button(self.frame, text='new game', command=self.new_game)
        self.button2 = Button(self.frame, text='exit', command=self.root.quit)
        self.button2.grid(row=5, column=0)
        self.button1.grid(row=5, column=6)
        self.frame.grid()
        self.root.mainloop()

    def new_game(self):
        self.frame.destroy()
        Start_page.Start_page(self.root)
