from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
        self.startGame = False
    

    def createWidgets(self):
        self.titleLabel = Label(self, text = "Homesick", font = "Helvetica 30", fg = "Red")
        self.titleLabel.grid(row = 0, column = 4, columnspan = 1)

        self.playButton = Button(self, text = "Play", command = self.playGame, font = "Times 20", fg = "Black")
        self.playButton.grid(row = 1, column = 1, columnspan = 2)
        
        
        self.musicButton = Button(self, text = "Music", command = self.playMusic, font = "Times 20", fg = "Black")
        self.musicButton.grid(row = 1, column = 3, columnspan = 2)
        
        self.difficultyButton = Button(self, text = "Difficulty", command = self.selectDifficulty, font = "Times 20", fg = "Black")
        self.difficultyButton.grid(row = 1, column = 5, columnspan = 2)

    def playGame(self):
        self.startGame = True
        
    def playMusic(self):
        master = Tk()
        w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        w2.pack()

    def selectDifficulty(self):
        column = 2

        allDifficulties = ["Easy", "Medium", "Hard"]
        for difficulty in allDifficulties:
            Radiobutton(self, text = difficulty).grid(row = 2, column = column)
            column += 2

root = Tk()
root.title("Homesick")
root.geometry("400x200")
app = Application(root)
root.mainloop()