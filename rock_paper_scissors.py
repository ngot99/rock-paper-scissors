import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from rock_paper_scissors_logic import RockPapperScissorGame 
from PIL import Image, ImageTk  
import random

# Defining a Move class to represent player's moves
class Move:
    def __init__(self, sign, player):
        self.sign = sign  # The move's sign (e.g., "Rock", "Paper", "Scissors")
        self.player = player  # The player who made the move (0 for player 1, 1 for player 2)

# Defining the main application class
class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Rock Paper Scissors Game")  # Setting the title of the application

        # Creating a container to hold different frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Dictionary to hold different frames of the application

        # Looping through different page classes and creating frames for each
        for F in (StartPage, GamePage, HowToPlayPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # Showing the start page initially

    # Function to switch between frames
    def show_frame(self, page, play_cpu=False):
        frame = self.frames[page]
        frame._play_cpu = play_cpu
        frame.tkraise()

# Start page class
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)

        # Title label
        title_label = tk.Label(self, text="Rock Paper Scissors", font=("Helvetica", 32, "bold"))
        title_label.grid(row=0, column=0, pady=100)

        # Initializing navigation buttons
        play_button = tk.Button(self, text="Play against a Friend", command=lambda: controller.show_frame(GamePage, play_cpu=False))
        play_button.grid(row=1, column=0, pady=5, padx=10)

        play_cpu_button = tk.Button(self, text="Play against a CPU Game", command=lambda: controller.show_frame(GamePage, play_cpu=True))
        play_cpu_button.grid(row=2, column=0, pady=5, padx=10)

        how_to_play_button = tk.Button(self, text="How to Play", command=lambda: controller.show_frame(HowToPlayPage))
        how_to_play_button.grid(row=3, column=0, pady=5, padx=10)

        tk.Label(self).grid(row=0, column=4)

# How to play page class
class HowToPlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)

        # Title label
        title_label = tk.Label(self, text="How to Play", font=("Helvetica", 32, "bold"))
        title_label.grid(row=0, column=0, pady=10)

        # Button to go back to main menu
        play_button = tk.Button(self, text="Main Menu", command=lambda: controller.show_frame(StartPage))
        play_button.grid(row=3, column=0, pady=10)

        # Text widget to display rules
        text_widget = tk.Text(self, wrap="word", font="Helvetica", width=100, height=15)
        text_widget.grid(row=2, column=0, padx=10, pady=10)

        # Reading rules from a file and displaying them in the text widget
        with open("rules.txt", "r") as file:
            content = file.read()
            text_widget.insert(tk.END,content)

# Game page class
class GamePage(tk.Frame):
    def __init__(self, parent, controller, play_cpu=False):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        self._game = RockPapperScissorGame()  # Creating an instance of the game logic class
        self._signs = self._game._signs  # Available signs in the game (e.g., "Rock", "Paper", "Scissors")
        self._valid_keys = self._game._valid_keys  # Valid keys for player input
        
        self._play_cpu = play_cpu  # Flag to indicate whether playing against CPU or not

        # Variables to track player moves
        self.p1_submitted = False
        self.p2_submitted = False
        self.p1_move = None
        self.p2_move = None

        self.player_labels = []  # Labels to display player options
        self.images = {}  # Dictionary to hold images for player options

        self._load_images()  # Loading images for player options
        self._create_screen()  # Creating game screen
        self._create_scoreboard()  # Creating scoreboard
        self.focus_set()

    # Function to load images for player options
    def _load_images(self):
        # Loading and resizing images for each option
        original_rock_image = Image.open("images/rock.png")
        resized_rock_image = original_rock_image.resize((50, 50))
        self.images["Rock"] = ImageTk.PhotoImage(resized_rock_image)

        original_paper_image = Image.open("images/paper.jpg")
        resized_paper_image = original_paper_image.resize((50, 50))
        self.images["Paper"] = ImageTk.PhotoImage(resized_paper_image)

        original_scissors_image = Image.open("images/scissors.jpg")
        resized_scissors_image = original_scissors_image.resize((50, 50))
        self.images["Scissors"] = ImageTk.PhotoImage(resized_scissors_image)


    # Function to create game screen
    def _create_screen(self):
        # Label to display game instructions
        self.label1 = tk.Label(self, text=f"First to {self._game.get_play_to()} wins!", font=("Helvetica", 32), bd=3, padx=15, pady=10)
        self.label1.grid(row=0, column=3, padx=5)

        # Player 1 options labels with corresponding images
        rock_label_p1 = tk.Label(self, text="Rock (A)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        rock_label_p1.grid(row=2, column=0, padx=5)
        self.player_labels.append(rock_label_p1)
        rock_label_p1.config(image=self.images["Rock"], compound=tk.TOP)

    def _create_screen(self):
        self.label1 = tk.Label(self, text=f"First to {self._game.get_play_to()} wins!", font=("Helvetica", 32), bd=3, padx=15, pady=10)
        self.label1.grid(row=0, column=3, padx=5)
         
         # Player 1 labels with blue borders
        rock_label_p1 = tk.Label(self, text="Rock (A)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        rock_label_p1.grid(row=2, column=0, padx=5)
        self.player_labels.append(rock_label_p1)
        rock_label_p1.config(image=self.images["Rock"], compound=tk.TOP)

        paper_label_p1 = tk.Label(self, text="Paper (S)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        paper_label_p1.grid(row=2, column=1, padx=5)
        self.player_labels.append(paper_label_p1)
        paper_label_p1.config(image=self.images["Paper"], compound=tk.TOP)

        scissors_label_p1 = tk.Label(self, text="Scissors (D)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        scissors_label_p1.grid(row=2, column=2, padx=5)
        self.player_labels.append(scissors_label_p1)
        scissors_label_p1.config(image=self.images["Scissors"], compound=tk.TOP)
        
        # Bind keys to labels
        self.bind("<a>", lambda event: self._wait_for_player(rock_label_p1, 0))
        self.bind("<s>", lambda event: self._wait_for_player(paper_label_p1, 0))
        self.bind("<d>", lambda event: self._wait_for_player(scissors_label_p1, 0))

        # Space between
        space_label = tk.Label(self, text="VS", font=("Helvetica", 12))
        space_label.grid(row=2, column=3, padx=5)
    
        # Player 2 labels with blue borders
        rock_label_p2 = tk.Label(self, text="Rock (J)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        rock_label_p2.grid(row=2, column=4, padx=5)
        self.player_labels.append(rock_label_p2)
        rock_label_p2.config(image=self.images["Rock"], compound=tk.TOP)

        paper_label_p2 = tk.Label(self, text="Paper (K)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        paper_label_p2.grid(row=2, column=5, padx=5)
        self.player_labels.append(paper_label_p2)
        paper_label_p2.config(image=self.images["Paper"], compound=tk.TOP)

        scissors_label_p2 = tk.Label(self, text="Scissors (L)", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        scissors_label_p2.grid(row=2, column=6, padx=5)
        self.player_labels.append(scissors_label_p2)
        scissors_label_p2.config(image=self.images["Scissors"], compound=tk.TOP)

        # Bind buttons to frame
        self.bind("<j>", lambda event: self._wait_for_player(rock_label_p2, 1))
        self.bind("<k>", lambda event: self._wait_for_player(paper_label_p2, 1))
        self.bind("<l>", lambda event: self._wait_for_player(scissors_label_p2, 1))
        quit_button = tk.Button(self, text="Quit Game", font=("Helvetica",12), bd=3, relief="ridge", 
                                command=lambda: [self._reset_game(), self.controller.show_frame(StartPage)])
        quit_button.grid(row=3, column=3, padx=5, pady=50)


    def _create_scoreboard(self):
        score = self._game.get_score()
        self.p1_score_label = tk.Label(self, text=f"P1 score: {score[0]}", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        self.p1_score_label.grid(row=0, column=0, padx=10)

        self.p2_score_label = tk.Label(self, text=f"P2 score: {score[1]}", font=("Helvetica", 12), bd=3, relief="ridge", padx=10, pady=5)
        self.p2_score_label.grid(row=0, column=6, padx=10)

    def _update_scoreboard(self):
        score = self._game.get_score()
        self.p1_score_label.config(text=f"Player 1: {score[0]}")
        self.p2_score_label.config(text=f"Player 2: {score[1]}")
        
    def _wait_for_player(self,label, player):
        if self._play_cpu:
            self._cpu_turn() 
        if self.p1_submitted == False or  self.p2_submitted == False:
            sign, key = label.cget("text").split()
             
            if player == 0:
                if self.p1_submitted == False:
                    self.p1_move = Move(sign,player)
                    self._grey_out(0)
                    self.p1_submitted = True     
            else:
                if self.p2_submitted == False:
                    self.p2_move = Move(sign,player)
                    self._grey_out(1)
                    self.p2_submitted = True            
            if self.p1_submitted and self.p2_submitted:
                self.after(1000, self.round_logic)
    
    def _cpu_turn(self):
        self.p2_move = Move(random.choice(self._signs), 1)
        self._grey_out(1)
        self.p2_submitted = True            

    # Greys out button to relect player has made move
    def _grey_out(self, player):
        if player == 0:
            for label in self.player_labels[:3]:
                label.config(bg="grey")
        elif player == 1:
            for label in self.player_labels[3:]:
                label.config(bg="grey")
        else:
            for label in self.player_labels:
                label.config(bg="grey")

    # Highlights winner of the round
    def _highlight_winner(self,round_winnner):
        if round_winnner == 0:
             for label in self.player_labels:
                if self.p1_move.sign in label.cget("text"):
                    label.config(bg="yellow")
        elif round_winnner < 0:
            for label in self.player_labels[:3]:
                if self.p1_move.sign in label.cget("text"):
                    label.config(bg="green")
            for label in self.player_labels[3:]:
                if self.p2_move.sign in label.cget("text"):
                    label.config(bg="red")
        else:
            for label in self.player_labels[:3]:
                if self.p1_move.sign in label.cget("text"):
                    label.config(bg="red")
            for label in self.player_labels[3:]:
                if self.p2_move.sign in label.cget("text"):
                    label.config(bg="green")

    # Reset buttons for new round/game
    def _reset_buttons(self):
        self.p1_submitted = False
        self.p2_submitted = False
        for label in self.player_labels:
                label.config(bg="white")

    # Resets buttons and score to simulate a new game
    def _reset_game(self):
        self._reset_buttons()
        self._game.reset_game()
        self._update_scoreboard()
        
    def _ask_replay(self): 
        return messagebox.askquestion(f"Game Over! Player {self._game.get_winner()+1} wins!", "Do you want to play again?")
         
    def round_logic(self):
        self._game.round_outcome(self.p1_move, self.p2_move)
        self._update_scoreboard()
        self._highlight_winner(self._game.get_round_winner())
        if self._game.has_winner():
            if self._ask_replay() == "yes":
                self._reset_game()
            else:  
                self._reset_game()
                self.controller.show_frame(StartPage)
            #msg = f'Player {self._game.get_winner()+1}  wins!'
            #self._label1["text"] = (msg,"black")
        else:
            self._game.reset_round()
            self.after(2000, self._reset_buttons)
        

if __name__ == "__main__":
    app = RockPaperScissorsApp()
    app.geometry("1100x800")
    app.mainloop()
