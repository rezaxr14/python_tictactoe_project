import itertools
from tkinter import Tk, Canvas, font, CENTER
import Constants
from PIL import Image, ImageTk


# creating the ticktacktoe class which extends Tk class and adds the game logic and aesthetics to the class
# For simplicity I didn't use Setter(s) and Getter(s) in this project
class Ticktacktoe(Tk):
    width, height = Constants.WIDTH, Constants.HEIGHT
    player = "X"
    background = "gray"
    already_clicked = [False for _ in range(9)]
    x_moves = []
    o_moves = []
    win= []
    x_image: ImageTk.PhotoImage
    o_image: ImageTk.PhotoImage
    def_image: ImageTk.PhotoImage
    background_image: ImageTk.PhotoImage
    background_image2: ImageTk.PhotoImage
    restart_image: ImageTk.PhotoImage
    change_image: ImageTk.PhotoImage
    x_win_image: ImageTk.PhotoImage
    o_win_image: ImageTk.PhotoImage
    no_winner_image: ImageTk.PhotoImage
    combo = []
    game_over = False
    game_over_message: Canvas.create_text

    def __init__(self):
        super().__init__()
        # set window size
        self.geometry(f"{self.width}x{self.height}")
        # set resizable to False
        self.resizable(width=False, height=False)
        self.title("Tik Tac Toe!")
        self.iconbitmap(Constants.icon)
        # All the wining combo
        self.win = self.all_wining_combo_maker(Constants.WIN)
        # Image
        self.x_image = ImageTk.PhotoImage(Image.open(Constants.x_path))
        self.o_image = ImageTk.PhotoImage(Image.open(Constants.o_path))
        self.def_image = ImageTk.PhotoImage(Image.open(Constants.def_path))
        self.background_image = ImageTk.PhotoImage(Image.open(Constants.background_path))
        self.background_image2 = ImageTk.PhotoImage(Image.open(Constants.background_path2))
        self.restart_image = ImageTk.PhotoImage(Image.open(Constants.restart_path))
        self.change_image = ImageTk.PhotoImage(Image.open(Constants.change_path))
        self.x_win_image = ImageTk.PhotoImage(Image.open(Constants.x_win_path))
        self.o_win_image = ImageTk.PhotoImage(Image.open(Constants.o_win_path))
        self.no_winner_image = ImageTk.PhotoImage(Image.open(Constants.no_winner_path))
        # creating a tkinter Canvas
        self.can = Canvas(self, height=self.height, width=self.width)
        self.can.create_image(300, 300, image=self.background_image, tag="background")
        self.font = font.Font(family='Helvetica', size=32, weight='bold')
        self.title = self.can.create_text(60 * 5, 35, fill='#6c19ab', font=self.font, text="Tic Tac Toe Game!")
        # making game tiles and putting them in place
        self.initialize_coordination(self.can)
        self.can.pack(anchor=CENTER)

    def all_wining_combo_maker(self, o_win=Constants.WIN):
        # permuting over the basic win combo
        for w in o_win:
            self.combo.extend((itertools.permutations(w, 3)))
        return self.combo

    def clicked(self, coordinates):
        # finding the closest item and getting its tag
        item = self.can.find_closest(coordinates.x, coordinates.y)
        item_tag = self.can.gettags(item[0])[0]
        # last character of tag names resemble their respected already_clicked indexes
        if self.player == "X" and self.already_clicked[int(item_tag[-1])] is False:
            self.can.itemconfig(item_tag, image=self.x_image)
            self.x_moves.append(int(item_tag[-1]))
            self.player = "O"
            self.already_clicked[int(item_tag[-1])] = True
            self.check_win()
        elif self.player == "O" and self.already_clicked[int(item_tag[-1])] is False:
            self.can.itemconfig(item_tag, image=self.o_image)
            self.o_moves.append(int(item_tag[-1]))
            self.player = "X"
            self.already_clicked[int(item_tag[-1])] = True
            self.check_win()

    def initialize_coordination(self, canvas: Canvas) -> None:
        for i in range(9):
            match i:
                case 0:
                    x_coordination, y_coordination = 150, 150
                case 1:
                    x_coordination, y_coordination = 60 * 5, 150
                case 2:
                    x_coordination, y_coordination = 60 * 7 + 25, 150
                case 3:
                    x_coordination, y_coordination = 150, 150 * 2
                case 4:
                    x_coordination, y_coordination = 60 * 5, 150 * 2
                case 5:
                    x_coordination, y_coordination = 60 * 7 + 25, 150 * 2
                case 6:
                    x_coordination, y_coordination = 150, 150 * 3
                case 7:
                    x_coordination, y_coordination = 60 * 5, 150 * 3
                case 8:
                    x_coordination, y_coordination = 60 * 7 + 25, 150 * 3
            # creating the game tiles
            # noinspection PyUnboundLocalVariable
            canvas.create_image(x_coordination, y_coordination, image=self.def_image, tag=f"cell{i}")
            canvas.tag_bind(f"cell{i}", "<Button-1>", self.clicked)
        # creating the restart button
        canvas.create_image(200, 565, image=self.restart_image, tag=f"restart")
        canvas.tag_bind(f"restart", "<Button-1>", self.restart)
        # creating the change the background button
        canvas.create_image(400, 555, image=self.change_image, tag=f"change")
        canvas.tag_bind(f"change", "<Button-1>", self.alternate_background)

    def check_win(self):

        if len(self.x_moves) >= 3:
            # checking all the possible 3 value pairs
            x_moves_combo = itertools.combinations(self.x_moves, 3)
            o_moves_combo = itertools.combinations(self.o_moves, 3)
            for x in x_moves_combo:
                if x in self.win:
                    self.can.create_image(300, 300, image=self.x_win_image, tag="play_again")
                    self.can.tag_bind("play_again", "<Button-1>", self.play_again)
                    self.game_over = True

            for o in o_moves_combo:
                if o in self.win:
                    self.can.create_image(300, 300, image=self.o_win_image, tag="play_again")
                    self.can.tag_bind("play_again", "<Button-1>", self.play_again)
                    self.game_over = True
            
            if self.already_clicked == [True for _ in range(9)] and self.game_over == False:
                self.can.create_image(300, 300, image=self.no_winner_image, tag="play_again")
                self.can.tag_bind("play_again", "<Button-1>", self.play_again)
                self.game_over = True

            if self.game_over is True:
                self.game_over_message = self.can.create_text(300, 520, font=self.font,
                                                              text="Click anywhere to play again!", fill='#6c19ab')

    def restart(self, event):
        # restoring the initial state
        self.player = "X"
        self.already_clicked = [False for _ in range(9)]
        self.x_moves = []
        self.o_moves = []
        for i in range(9):
            self.can.itemconfig(f"cell{i}", image=self.def_image)

    def play_again(self, event):
        # deleting the winner state from canvas
        self.game_over = False
        self.can.delete(self.game_over_message)
        self.can.delete("play_again")
        self.restart(event)

    def alternate_background(self, event):
        # changing the background image
        if self.background == "gray":
            self.background = "pink"
            self.can.itemconfig("background", image=self.background_image)
        elif self.background == "pink":
            self.background = "gray"
            self.can.itemconfig("background", image=self.background_image2)


def main():
    root = Ticktacktoe()
    get_text(root, root.can)
    get_background_color(root)
    get_already_clicked(root)
    root.mainloop()


def get_text(r, c):
    return c.itemcget(r.title, "text")


def get_background_color(r):
    return r.background


def get_already_clicked(r):
    return r.already_clicked


if __name__ == '__main__':
    main()
