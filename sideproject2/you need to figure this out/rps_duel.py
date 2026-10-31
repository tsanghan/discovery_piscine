#!/usr/bin/env python

from getpass import getpass
import sys

player1_wins = [
    ('r','s'),
    ('s','p'),
    ('p', 'r')
]

players_draw = [
    ('r','r'),
    ('s','s'),
    ('p', 'p')
]

choice_question_str = 'what is your choice? r=Rock, p=Paper, or s=Scissors\n'


def add_and_print(players: dict[str, list[int]], round: int, number: int):
    players[list(players.keys())[number]].append(1)
    print(f"Rount {round}: Player {list(players.keys())[number]} wins!!")

def main():
    ''' main() '''
    players: dict[str, list[int]] = {}
    for number in range(0,2):
        players[input(f"What is Player{number+1}'s name? ")] = []

    for round in range(0,3):
        print('#' * 80)
        print(f"Round {round}")
        players_choice: list[str] = []
        for number in range(0,2):
            try:
                while player_choice := getpass(f"Player {list(players.keys())[number]} "
                                            f"{choice_question_str}")[0].lower():
                    if player_choice in ('r', 'p', 's'):
                        players_choice.append(player_choice)
                        break
            except IndexError:
                print(f"Please only enter 'r', 'p' or 's'.")
                sys.exit()

        # if tuple(players_choice) in player1_wins:
        #     add_and_print(players, round, 0)
        # elif tuple(players_choice) in players_draw:
        #     pass
        # else:
        #     add_and_print(players, round, 1)

        match players_choice:
            case x if tuple(x) in player1_wins:
                add_and_print(players, round, 0)
            case x if tuple(x) in players_draw:
                pass
            case _:
                add_and_print(players, round, 1)

    player1_name, player2_name = tuple(list(players.keys()))
    player1_score, player2_score = map(sum, tuple(list(players.values())))

    print(f"{'#' * 80}\nGrand Finale!!")
    print(f"Player {player1_name} scored {player1_score}\n"
          f"Player {player2_name} scored {player2_score}")

    if player1_score > player2_score:
        print(f"Player {player1_name} is the Grand Champion!!")
    elif player1_score == player2_score:
        print(f"Both Player {player1_name} & "
              f"Player {player1_name} are the Grand Champions!!")
    else:
        print(f"Player {player2_name} is the Grand Champion!!")

if __name__ == '__main__':
    main()