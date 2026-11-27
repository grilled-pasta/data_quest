#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_data_alchemist.py                               :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:49:18 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 10:49:22 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

from random import randrange

players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
           "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===")

    print("\nInitial list of players:", players)

    all_capitalized = [player.capitalize() for player in players]
    print("New list with all names capitalized:", all_capitalized)

    capitalized = [player for player in players if player[0].isupper()]
    print("New list of capitalized names only:", capitalized)

    scores = {player: randrange(0, 1000) for player in players}
    print("Score dict:", scores)

    average = sum(scores.values()) / len(scores)
    print(f"Score average is {average:.2f}")

    high_scores = {
        player: score
        for player, score in scores.items()
        if score > average
    }
    print("High scores", high_scores)


if __name__ == "__main__":
    main()
