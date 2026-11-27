#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_achievement_tracker.py                          :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:48:48 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 10:48:53 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

import random

# feedback allow random(), provide a full list of achievements

achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
        ]


def get_player_achievements() -> set[str]:
    count = random.randint(len(achievements) // 3, len(achievements) // 2)
    return set(random.sample(achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = get_player_achievements()
    bob = get_player_achievements()
    charlie = get_player_achievements()
    dylan = get_player_achievements()
    all_achievements = alice.union(bob, charlie, dylan)

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("\nAll distinct achievements:", all_achievements)
    print("\nCommon achievements:",
          alice.intersection(bob, charlie, dylan))
    print("\nOnly Alice has:",
          alice.difference(bob, charlie, dylan))
    print("Only Bob has:",
          bob.difference(alice, charlie, dylan))
    print("Only Charlie has:",
          charlie.difference(alice, bob, dylan))
    print("Only Dylan has:",
          dylan.difference(alice, bob, charlie))
    print("\nAlice is missing:",
          all_achievements.difference(alice))
    print("\nBob is missing:",
          all_achievements.difference(bob))
    print("\nCharlie is missing:",
          all_achievements.difference(charlie))
    print("\nDylan is missing:",
          all_achievements.difference(dylan))


if __name__ == "__main__":
    main()
