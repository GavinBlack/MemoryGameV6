# Pizza Panic
# Player must catch falling pizzas before they hit the ground

from livewires import games, color
import random, time, pygame
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

games.init(screen_width = 640, screen_height = 480, fps = 60)


class SmallSprite(games.Sprite):
        #Initialize class variables
        image = games.load_image("images/smallSprite.png")

        def __init__(self):
                super(SmallSprite, self).__init__(image = SmallSprite.image, x = games.mouse.x,y = games.mouse.y)

        def update(self):
                self.x = games.mouse.x
                self.y = games.mouse.y 

class Card(games.Sprite):
        #Load in images, create class variables
        blocker_image = games.load_image("images/blocker.png")
        bird_image = games.load_image("images/bird.png")
        elephant_image = games.load_image("images/elephant.png")
        spider_image = games.load_image("images/spider.png")
        grape_image = games.load_image("images/grapes.png")
        peach_image = games.load_image("images/peach.png")
        pears_image = games.load_image("images/pears.png")
        cheetah_image = games.load_image("images/cheetah.png")
        chicken_image = games.load_image("images/chicken.png")
        eagle_image = games.load_image("images/eagle.png")
        guido_image = games.load_image("images/guido.png")
        lion_image = games.load_image("images/lion.png")
        tiger_image = games.load_image("images/tiger.png")

        easyLives = 10
        hardLives = 5
        totalAttempts = 0
        cardsShowing = 0
        time = 0
        clickedCards = []
        clickable = True
        
        def __init__(self,difficulty,world,x,y,whichImage = 1):
                super(Card,self).__init__(image = Card.blocker_image, x=x,y=y)

                #create instance variables for future use
                self.world = world
                self.whichImage = whichImage
                self.clicked = False
                self.difficulty = difficulty

        def cardClicked(self):
                if Card.clickable: #if the card is clickable
                        for sprite in self.overlapping_sprites:
                                for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN: #if it was a click
                                                if event.button == 1: #if a left click
                                                        if not self.clicked: #can't click same image twice
                                                                if self.whichImage == 1:
                                                                        self.image = Card.bird_image
                                                                elif self.whichImage == 2:
                                                                        self.image = Card.elephant_image
                                                                elif self.whichImage == 3:
                                                                        self.image = Card.spider_image
                                                                elif self.whichImage == 4:
                                                                        self.image = Card.grape_image
                                                                elif self.whichImage == 5:
                                                                        self.image = Card.peach_image
                                                                elif self.whichImage == 6:
                                                                        self.image = Card.pears_image
                                                                elif self.whichImage == 7:
                                                                        self.image = Card.cheetah_image
                                                                elif self.whichImage == 8:
                                                                        self.image = Card.chicken_image
                                                                elif self.whichImage == 9:
                                                                        self.image = Card.eagle_image
                                                                elif self.whichImage == 10:
                                                                        self.image = Card.guido_image
                                                                elif self.whichImage == 11:
                                                                        self.image = Card.lion_image
                                                                elif self.whichImage == 12:
                                                                        self.image = Card.tiger_image

                                                                self.clicked = True
                                                                Card.cardsShowing += 1
                                                                Card.clickedCards.append(self)

        def checkIfSameCard(self):
                """
                 if two cards are showing, make it so the
                 user can't click anymore cards. Calculate
                 time that the user sees both cards before
                 either destroying them, or putting them
                 back to the card image.
                """
                if self.difficulty == 1: #if on easy mode
                        if Card.cardsShowing == 2: #if 2 cards are showing, figure out what to do
                                Card.clickable = False
                                Card.time += 1
                                if Card.time == games.screen.fps * 8: #timer for letting the cards display
                                        for card in Card.clickedCards:
                                                #if both images are the same
                                                if Card.clickedCards[0].whichImage == Card.clickedCards[1].whichImage:
                                                        card.destroy()
                                                        self.world.score.value += 5
                                                        self.world.totalCards -= 1
                                                        
                                                        if self.world.totalCards == 0: #if there are no more cards, trigger the nextLevel function after a few seconds
                                                                level_message = games.Message(value = "Level " + str(self.world.level+1),
                                                                                size = 40,
                                                                                color = color.yellow,
                                                                                x = games.screen.width/2,
                                                                                y = games.screen.width/10,
                                                                                lifetime = 5 * games.screen.fps,
                                                                                after_death = self.nextLevel,
                                                                                is_collideable = False)
                                                                games.screen.add(level_message)
                                        
                                                else: #if cards don't match, replace with blocker image and make it so they are clickable again
                                                        Card.clickedCards[0].image = Card.blocker_image
                                                        Card.clickedCards[1].image = Card.blocker_image
                                                        Card.clickedCards[0].clicked = False
                                                        Card.clickedCards[1].clicked = False
                                                        Card.totalAttempts += .5
                                                        
                                                        if int(Card.totalAttempts) == Card.easyLives:
                                                                gameover = games.Message(value = "Game Over",
                                                                                size = 70,
                                                                                color = color.red,
                                                                                x = games.screen.width/2,
                                                                                y = games.screen.width/2-100,
                                                                                lifetime = 5 * games.screen.fps,
                                                                                after_death = games.screen.quit,
                                                                                is_collideable = False)
                                                                games.screen.add(gameover)
                
                                        Card.time = 0
                                        Card.clickedCards = []
                                        Card.cardsShowing = 0
                                        Card.clickable = True
                else: #if on a mode other than easy
                        if Card.cardsShowing == 3: #if 3 cards are showing, figure out what to do with them
                                Card.clickable = False
                                Card.time += 1
                                if Card.time == games.screen.fps * 8: #timer for letting the cards display
                                        for card in Card.clickedCards:
                                                #if all images are the same
                                                if Card.clickedCards[0].whichImage == Card.clickedCards[1].whichImage and Card.clickedCards[0].whichImage == Card.clickedCards[2].whichImage:
                                                        card.destroy()
                                                        self.world.score.value += 5
                                                        self.world.totalCards -= 1
                                                        
                                                        if self.world.totalCards == 0: #if there are no more cards, trigger the nextLevel function after a few seconds
                                                                level_message = games.Message(value = "Level " + str(self.world.level+1),
                                                                                size = 40,
                                                                                color = color.yellow,
                                                                                x = games.screen.width/2,
                                                                                y = games.screen.width/10,
                                                                                lifetime = 5 * games.screen.fps,
                                                                                after_death = self.nextLevel,
                                                                                is_collideable = False)
                                                                games.screen.add(level_message)
                                         
                                                else: #if cards don't match, replace with blocker image and make it so they are clickable again
                                                        Card.clickedCards[0].image = Card.blocker_image
                                                        Card.clickedCards[1].image = Card.blocker_image
                                                        Card.clickedCards[2].image = Card.blocker_image
                                                        Card.clickedCards[0].clicked = False
                                                        Card.clickedCards[1].clicked = False
                                                        Card.clickedCards[2].clicked = False
                                                        Card.totalAttempts += .5
                                                        
                                                        if int(Card.totalAttempts) == Card.hardLives:
                                                                gameover = games.Message(value = "Game Over",
                                                                                size = 70,
                                                                                color = color.red,
                                                                                x = games.screen.width/2,
                                                                                y = games.screen.width/2-100,
                                                                                lifetime = 5 * games.screen.fps,
                                                                                after_death = games.screen.quit,
                                                                                is_collideable = False)
                                                                games.screen.add(gameover)

                                        Card.time = 0
                                        Card.clickedCards = []
                                        Card.cardsShowing = 0
                                        Card.clickable = True
                        
                
        def update(self):
                self.cardClicked()
                self.checkIfSameCard()

        def nextLevel(self):
                """
                Reset most variables for the new level
                Make sure not to exceed the row limit
                Rebuild the board based on difficulty
                """
                Card.time = 0
                Card.clickedCards = []
                Card.cardsShowing = 0
                Card.clickable = True
                Card.totalAttempts = 0
                
                if self.world.level == 0:
                        self.world.level += 2

                if World.level < World.max_rows:
                        World.rows += 1

                world = World()
                World.totalCards = World.rows * World.cols
                World.level += 1
                World.cards = []
                world.createBoard(self.difficulty)

class World(object):
        #Initialize class variables
        cards = []
        allCards = []
        rows = 1
        cols = 6
        totalCards = rows * cols
        level = 1
        max_rows = 4
        difficultyLabel = ""
        alreadyDisplayed = False

        score = games.Text(value = 0,
                                size = 30,
                                color = color.green,
                                top = 5,
                                right = games.screen.width - 25,
                                is_collideable = False)
        games.screen.add(score)
        

        """
         fill up the card list based on the total
         amount of cards, shuffle it, reassign it
         to the class variable named cards
        """
        def fillCardArray(self,difficulty):
                if difficulty == 1: #if easy, fill list with pairs of 2s
                        if World.level == 1:
                                for i in range(1,World.totalCards//2+1):
                                        World.cards.append(i)
                                        World.cards.append(i)
                                random.shuffle(World.cards)
                        else: 
                                World.allCards = []
                                for i in range(1,World.totalCards//2+1):
                                        World.allCards.append(i)
                                        World.allCards.append(i)
                                random.shuffle(World.allCards)

                                ct = 0
                                for i in range(World.rows):
                                        tempList = []
                                        for j in range(1,World.cols+1):
                                                tempList.append(World.allCards[ct])
                                                if j % World.cols == 0:
                                                        random.shuffle(tempList)
                                                        World.cards.append(tempList)
                                                ct += 1
                else: #if not easy, fill list with pairs of 3s
                        if World.level == 1:
                                for i in range(1,World.totalCards//3+1):
                                        World.cards.append(i)
                                        World.cards.append(i)
                                        World.cards.append(i)
                                random.shuffle(World.cards)
                        else:
                                World.allCards = []
                                for i in range(1,World.totalCards//3+1):
                                        World.allCards.append(i)
                                        World.allCards.append(i)
                                        World.allCards.append(i)
                                random.shuffle(World.allCards)

                                ct = 0
                                for i in range(World.rows):
                                        tempList = []
                                        for j in range(1,World.cols+1):
                                                tempList.append(World.allCards[ct])
                                                if j % World.cols == 0:
                                                        random.shuffle(tempList)
                                                        World.cards.append(tempList)
                                                ct += 1
                        
        """
         create and add the cards to the screen
         in the correct format
        """
        def createBoard(self, difficulty):
                x = 65
                y = 40
                xSeparator = 95
                ySeparator = 95
                card = None
                difficultyText = ""
                
                if not World.alreadyDisplayed:
                        if difficulty == 1:
                                difficultyText = "Difficulty: Easy --- Match 2 Cards"
                        else:
                                difficultyText = "Difficulty: Hard --- Match 3 Cards"
                                
                        lblDifficulty = games.Message(value = difficultyText,
                                        size = 34,
                                        color = color.green,
                                        top = games.screen.height/2-15,
                                        right = games.screen.width - (games.screen.width - 500),
                                        lifetime = games.screen.fps * 6,
                                        is_collideable = False)
                        games.screen.add(lblDifficulty)
                        World.alreadyDisplayed = True

                self.fillCardArray(difficulty)
                
                if World.level == 1: #if level one, create board based on list indexes
                        for i in range(World.totalCards):
                                if World.cards[i] == 1:
                                        card = Card(difficulty=difficulty,world = self, x = x+i*xSeparator, y = 68,whichImage = 1)
                                elif World.cards[i] == 2:
                                        card = Card(difficulty=difficulty,world = self, x = x+i*xSeparator, y = 68, whichImage = 2)
                                elif World.cards[i] == 3:
                                        card = Card(difficulty=difficulty,world = self, x = x+i*xSeparator, y = 68, whichImage = 3)
                                games.screen.add(card)
                else: #if not level 1, create the board based on the 2D cards list
                        for i in range(World.rows):
                                for j in range(World.cols):
                                        if World.cards[i][j] == 1:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator)
                                        elif World.cards[i][j] == 2:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=2)
                                        elif World.cards[i][j] == 3:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=3)
                                        elif World.cards[i][j] == 4:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=4)
                                        elif World.cards[i][j] == 5:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=5)
                                        elif World.cards[i][j] == 6:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=6)
                                        elif World.cards[i][j] == 7:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=7)
                                        elif World.cards[i][j] == 8:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=8)
                                        elif World.cards[i][j] == 9:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=9)
                                        elif World.cards[i][j] == 10:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=10)
                                        elif World.cards[i][j] == 11:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=11)
                                        elif World.cards[i][j] == 12:
                                                card = Card(difficulty=difficulty,world = self, x=x+j*xSeparator,y=y+i*ySeparator,whichImage=12)
                                        games.screen.add(card)

class TkPygame:
    #1 -> easy, 2 -> hard
    difficulty = 1
        
    def __init__(self):

        self.tk_root = tk.Tk()
        self.tk_root.geometry("290x300")
        self.tk_root.title("Memory Game")
        #self.tk_root["background"] = "white"
        
        #create menu bar
        menuBar = Menu()
        self.tk_root.config(menu=menuBar)

        fileMenu = Menu(menuBar,tearoff=0)
        #add commands if neeeded here
        #if more than 1 command, add separator
        fileMenu.add_command(label="Exit",command=lambda: TkPygame._quit(self.tk_root))
        menuBar.add_cascade(label="File",menu=fileMenu)

        #adds help tab
        helpMenu = Menu(menuBar,tearoff=0)
        helpMenu.add_command(label="Directions")
        menuBar.add_cascade(label="Help",menu=helpMenu)
        
        self.make_tk_widgets()

        self.tk_root.mainloop()

    def _quit(win):
        win.quit()
        win.destroy()
        exit()

    def make_tk_widgets(self):
        """
        Create the widgets on the main tkinter screen
        """      
        self.memory_game_label = ttk.Label(self.tk_root,text="Memory Game")
        self.memory_game_label.grid(row=1,column=3)
        self.directions_button = ttk.Button(self.tk_root,text="Directions",command=self.toggle_directions)
        self.directions_button.grid(row=2,column=3,padx=30,pady=15)
        
        self.easy_button = ttk.Button(self.tk_root,text="Easy",command=lambda: self.change_difficulty(1))
        self.easy_button.grid(row=3,column=2)
        self.hard_button = ttk.Button(self.tk_root,text="Hard",command=lambda: self.change_difficulty(2))
        self.hard_button.grid(row=3,column=4)
        self.start_button = ttk.Button(self.tk_root,text="Start",command=self.toggle_to_game)
        self.start_button.grid(row=4,column=3,pady=15)
        
    def toggle_to_game(self):
        #widthdraws from tkinter window and starts the livewires game
        self.tk_root.withdraw()
        self.main()

    def change_difficulty(self, difficulty):
        if difficulty == 1:
            TkPygame.difficulty = 1
        else:
            TkPygame.difficulty = 2
        
    def toggle_directions(self):
        #if user hit directions button, hide main screen buttons and reveal directions page buttons
        self.memory_game_label.grid_forget()
        self.directions_button.grid_forget()
        self.easy_button.grid_forget()
        self.hard_button.grid_forget()
        
        self.directions_label = ttk.Label(self.tk_root, text="The goal of the game is to\n match the two cards together.\nIf the two cards don't match, they\nwill flip back over.\n Easy: Match 2 cards\nHard: Match 3 cards")
        self.directions_label.grid(padx=60,pady=0)
        self.back_from_directions = ttk.Button(self.tk_root,text="Back",command=self.back_from_directions)
        self.back_from_directions.grid(padx=110,pady=20)
        self.start_button.grid(row=4,column=3,pady=15)

    def back_from_directions(self):
        self.directions_label.grid_forget()
        self.back_from_directions.grid_forget()
        self.memory_game_label.grid(row=1,column=3)
        self.directions_button.grid(row=2,column=3,padx=30,pady=15)
        self.easy_button.grid(row=3,column=2)
        self.hard_button.grid(row=3,column=4)

        
    def main(self):
        background_image = games.load_image("images/background.jpg", transparent = False)
        
        games.screen.background = background_image
        games.mouse.is_visible = True
        
        world = World()
        world.createBoard(TkPygame.difficulty)
        
        smallCursor = SmallSprite()
        games.screen.add(smallCursor)
        
        games.screen.mainloop()

TkPygame()
