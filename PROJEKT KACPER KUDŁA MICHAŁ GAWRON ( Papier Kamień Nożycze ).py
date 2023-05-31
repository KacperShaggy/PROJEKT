import random
import termcolor

print("Witaj w grze Papier, Kamień, Nożyce! \n")

moves = ["papier", "kamień", "nożyce"]

player_score = 0
computer_score = 0

while True:
    print(f"  {termcolor.colored('KOMPUTER', 'blue')}")
    print(" __________")
    print(f" {moves.index('papier')+1} - {termcolor.colored('papier', 'blue')} ")
    print(f" {moves.index('kamień')+1} - {termcolor.colored('kamień', 'grey')} ")
    print(f" {moves.index('nożyce')+1} - {termcolor.colored('nożyce', 'red')}")
    print(" __________\n")
    print(f"     {termcolor.colored('TY', 'red')}\n")

    player_move_index = input("Twój ruch (podaj numer opcji): ")

    try:
        player_move_index = int(player_move_index)
        player_move = moves[player_move_index-1]
    except (ValueError, IndexError):
        print("Miała być liczba z przedziału 1-3!")
        continue

    computer_move = random.choice(moves)

    if computer_move == "papier":
        print(f"{termcolor.colored('Komputer wybrał', 'white')} {termcolor.colored('papier', 'blue')} ")
    elif computer_move == "kamień":
        print(f"{termcolor.colored('Komputer wybrał', 'white')}{termcolor.colored('kamień', 'grey')} ")
    else:
        print(f"{termcolor.colored('Komputer wybrał', 'white')} {termcolor.colored('nożyce', 'red')} ")

    if player_move == "papier":
        if computer_move == "papier":
            print(f"{termcolor.colored('REMIS!', 'white')}")
        elif computer_move == "kamień":
            print(f"{termcolor.colored('WYGRAŁEŚ!', 'green')}")
            player_score += 1
        elif computer_move == "nożyce":
            print(f"{termcolor.colored('PRZEGRAŁEŚ!', 'red')}")
            computer_score += 1
    elif player_move == "kamień":
        if computer_move == "papier":
            print(f"{termcolor.colored('PRZEGRAŁEŚ!', 'red')}")
            computer_score += 1
        elif computer_move == "kamień":
            print(f"{termcolor.colored('REMIS!', 'white')}")
        elif computer_move == "nożyce":
            print(f"{termcolor.colored('WYGRAŁEŚ!', 'green')}")
            player_score += 1
    elif player_move == "nożyce":
        if computer_move == "papier":
            print(f"{termcolor.colored('WYGRAŁEŚ!', 'green')}!")
            player_score += 1
        elif computer_move == "kamień":
            print(f"{termcolor.colored('PRZEGRAŁEŚ!', 'red')}")
            computer_score += 1
        elif computer_move == "nożyce":
                print(f"{termcolor.colored('REMIS!', 'white')}")
       
    print(f"\n{termcolor.colored('Wynik:', 'cyan')} Gracz: {player_score} | Komputer: {computer_score}\n")

    play_again = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
    if play_again.lower() == "nie":
        print("Dziękujemy za grę!")
        break