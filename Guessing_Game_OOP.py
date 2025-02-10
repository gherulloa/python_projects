from random import randint
from time import sleep
from os import system

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class GuessNumber:
    def __init__(self):
        self.number_to_guess = 0
        self.attempts = 0
        self.players = []
        self.playing = True
    
    def play(self):
        self.number_to_guess = randint(1, 5)
        print("Welcome to the guessing game. \nGuess the number I'm thinking (only numbers between 1 and 100). \nGood luck!")
        
        while True:
            try:
                guess = int(input("Type your guess: "))
                print("Okay, let me see...")
                sleep(3)
                system('clear')
            except ValueError:
                print("Come on. That's not a number.")
                continue

            if 1 <= guess <= 100:
                if guess > self.number_to_guess:
                    print("Nope, that's too high! Try again.")
                    self.attempts += 1
                elif guess < self.number_to_guess:
                    print("Try again, that's too low!")
                    self.attempts += 1
                else:
                    print(f"You got it! The correct number was {self.number_to_guess}.\nAnd it only took you {self.attempts} tries to get it!")
                    self.save_score()
                    break
            else:
                print("Please only try numbers between 1 and 100.")
    
    def save_score(self):
        name = input("What is your name? ")
        for player in self.players:
            if player.name == name:
                player.score = self.attempts
                break
        else:
            self.players.append(Player(name, self.attempts))

        self.players = sorted(self.players, key=lambda player: player.score)
        self.attempts = 0
    
    def show_score(self):
        print("\nSCOREBOARD:")
        for i, player in enumerate(self.players):
            print(f"{i + 1}. {player.name} - {player.score} attempts")
        
    def end_game(self):
        print("Thanks for playing. Here's the scoreboard: ")
        self.playing = False

#main code
game = GuessNumber()
while game.playing:
    game.play()
    game.show_score()
    sleep(5)
    system('clear') 
    if input("Do you want to play again? (y/n) ").lower() == "n":
        game.end_game()
        game.show_score()
    