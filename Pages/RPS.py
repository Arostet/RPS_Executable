import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class RPSGame():
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.games_played = 0
        self.init_splash_screen()

    def init_splash_screen(self):
        self.splash_root = tk.Tk()
        self.splash_root.overrideredirect(True)

        logo = Image.open("/Users/Micha/Documents/Programming/RPS/Assets/Images/rps.png")
        logo = ImageTk.PhotoImage(logo)

        logo_label = tk.Label(self.splash_root, image=logo)
        logo_label.image = logo  # Keep a reference!
        logo_label.pack()

        self.center_window(self.splash_root, logo.width(), logo.height())
        self.splash_root.after(3000, self.close_splash)
        self.splash_root.mainloop()
    
    def close_splash(self):
            # Destroy the splash screen and start the main application
            self.splash_root.destroy()
            self.init_main_window()

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    def init_main_window(self):
        self.root = tk.Tk()
        self.root.title("RPS Game")

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", foreground="blue", background="white", font=("Helvetica", 14), padding=6)


        # Buttons for Rock, Paper, Scissors
        self.rock_button = ttk.Button(self.mainframe, text="Rock", style="Custom.TButton", command=lambda: self.play('r'))
        self.rock_button.grid(column=1, row=1)
        self.paper_button = ttk.Button(self.mainframe, text="Paper",style="Custom.TButton", command=lambda: self.play('p'))
        self.paper_button.grid(column=2, row=1)
        self.scissors_button = ttk.Button(self.mainframe, text="Scissors",style="Custom.TButton", command=lambda: self.play('s'))
        self.scissors_button.grid(column=3, row=1)

        #Quit Button
        self.quit_button = tk.Button(self.mainframe, text="Quit", fg="red", bg="white", font=("Helvetica", 14), command=self.quit_game)
        self.quit_button.grid(column=4, row=4)

        #Previous Game Display
        self.prev_game_label = ttk.Label(self.mainframe, text="")
        self.prev_game_label.grid(column=2, row=4, columnspan=3)
        
        #Leaderboard Display
        self.leaderboard_label = ttk.Label(self.mainframe, text="")
        self.leaderboard_label.grid(column=2, row=4, columnspan=3)

        self.result_label = ttk.Label(self.mainframe, text="")
        self.result_label.grid(column=1, row=2, columnspan=3)

        self.leaderboard_label = ttk.Label(self.mainframe, text="")
        self.leaderboard_label.grid(column=2, row=3, columnspan=2)


        self.root.mainloop()

    def get_computer_rps(self):
        return random.choice(["r", "p", "s"])

    def update_game_result(self, user_choice, computer_choice):
        update_text = f"COMPUTER: {computer_choice.upper()} versus YOU: {user_choice.upper()}\n"
        if user_choice == computer_choice:
            update_text += "It's a tie!"
        elif (computer_choice == 'r' and user_choice == 's') or \
             (computer_choice == 's' and user_choice == 'p') or \
             (computer_choice == 'p' and user_choice == 'r'):
            update_text += "Computer wins!"
            self.computer_wins += 1

        else:
            update_text += "You win!"
            self.user_wins += 1


        self.result_label.config(text=update_text)
        self.games_played +=1
    
    def quit_game(self):
        print("Game ended. Thanks for playing!")
        self.update_leaderboard()  # Show the leaderboard
        self.root.destroy()  # This will close the GUI window

    def update_leaderboard(self):
        leaderboard_text = f"Games Played: {self.games_played}\n" \
                           f"Your Wins: {self.user_wins}\n" \
                           f"Computer Wins: {self.computer_wins}"
        if self.computer_wins > self.user_wins:
            leaderboard_text += "\nThe Computer is victorious for now."
        elif self.computer_wins < self.user_wins:
            leaderboard_text += "\nYou've proven yourself up to the challenge."
        else:
            leaderboard_text += "\nIt's a tie."
        
        self.leaderboard_label.config(text=leaderboard_text)
    def play(self,user_choice):
        #REMOVED WHILE LOOP TO HANDLE PLAY AS AN EVENT INSTEAD OF A LOOP FOR TKINTER
        computer_choice = self.get_computer_rps()
        self.update_game_result(user_choice, computer_choice)

        # self.get_game_result(user_choice, computer_choice)
        self.update_leaderboard() #DELETED show_..()


game = RPSGame()
# game.play()
