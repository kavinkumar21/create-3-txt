#apply in game
import sys
import random
from enum import Enum

def rps():
    game_count = 0
    python_wins = 0
    player_wins = 0

    def play_rps():
        playerchoice = input(
            "Enter...\n1 for Rock, \n2 for Paper, or \n3 for Cisor\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SICER = 3

        # print(playerchoice)
        player = int(playerchoice)

        comchoice = random.choice("123")
        computer = int(comchoice)
        print("")
        print(f"You Choose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.' , '')}.y")
        print("")

        def game_play(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                print("You Win!👌")
            elif player == 2 and computer == 1:
                player_wins += 1
                print("You Win!👌")
            elif player == 3 and computer == 2:
                player_wins += 1
                print("You Win!👌")
            elif player == computer:
                print("😁Game Tie")
            else:
                python_wins += 1
                print("🐍 Python Win")

        show_result = game_play(player, computer)
        print(show_result)

        nonlocal game_count
        game_count += 1
        print(f"Game Count :{str(game_count)}")
        print(f"\nPlayer wins:{str(player_wins)}")
        print(f"\nPython wins:{str(python_wins)}")
        print('\nPlay agan?')

        while True:
            playagain = input("\nY for Yes or \nQ to Quite\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit("Buy👋")

    return play_rps

play = rps()

if __name__ == "__main__":
    play()

# print(__name__)