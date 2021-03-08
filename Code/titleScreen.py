from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
        self.startGame = False
        self.isEasy = False
        self.isMedium = False
        self.isHard = False
        self.volume = None

    

    def createWidgets(self):
        self.titleLabel = Label(self, text = "Homesick", font = "Helvetica 30", fg = "Red")
        self.titleLabel.grid(row = 0, column = 4, columnspan = 1)

        self.playButton = Button(self, text = "Play", command = self.playGame, font = "Times 20", fg = "Black")
        self.playButton.grid(row = 1, column = 1, columnspan = 2)
        
        
        self.musicButton = Button(self, text = "Music", command = self.playMusic, font = "Times 20", fg = "Black")
        self.musicButton.grid(row = 1, column = 3, columnspan = 2)
        
        self.difficultyLabel = Label(self, text = "Difficulty", font = "Times 20", fg = "Black")
        self.difficultyLabel.grid(row = 1, column = 5, columnspan = 2)

        self.option = IntVar()
        self.chooseEasy = Radiobutton(self, text = "Easy", variable = self.option, value = 1)
        self.chooseEasy.grid(row = 2, column = 5, sticky = W)
        self.chooseMedium = Radiobutton(self, text = "Medium", variable = self.option, value = 2)
        self.chooseMedium.grid(row = 4, column = 5, sticky = W)
        self.chooseHard = Radiobutton(self, text = "Hard", variable = self.option, value = 3)
        self.chooseHard.grid(row = 6, column = 5, sticky = W)

    def selectedButton(self):
        if self.option == 1:
            self.isEasy = True
            self.isMedium = False
            self.isHard = False
        elif self.option == 2:
            self.isEasy = False
            self.isMedium = True
            self.isHard = False
        elif self.option == 3:
            self.isEasy = False
            self.isMedium = False
            self.isHard = True


    def playGame(self):
        self.startGame = True
        
    def playMusic(self):
        master = Tk()
        w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        label1 = Label(master, text = "Volume")
        self.volume = w2.get()

        label1.grid(row=0, column=0)
        w2.grid(row=0, column=1)
        master.geometry("175x60")