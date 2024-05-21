import random

def roll():
    return random.randint(1, 6)

def main():
    while True:
        playernum = input("How many players do you want (between 2 to 4): ")
        if playernum.isdigit():
            playernum = int(playernum)
            if 1 < playernum <= 4:
                break
            else:
                print("Please enter a number between 2 to 4.")
        else:
            print("Invalid input. Try again.")

    maxscore = 50
    playerscore = [0 for _ in range(playernum)]

    while max(playerscore) < maxscore:
        for i in range(playernum):
            print(f"\nPlayer {i + 1}'s turn has just started!")
            print(f"Your total score is: {playerscore[i]}")
            current_score = 0
            while True:
                ask = input("Do you want to roll? (y/n) ").lower()
                if ask != 'y':
                    break
                value = roll()
                if value == 1:
                    print("You rolled a 1, Your turn is done.")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a: {value}")
            playerscore[i] += current_score
            print(f"Your total score is now: {playerscore[i]}")
            if playerscore[i] >= maxscore:
                break

    maxo = max(playerscore)
    winning = playerscore.index(maxo)
    print(f"The winner is player {winning + 1} with a score of {playerscore[winning]}!")

if __name__ == "__main__":
    main()
