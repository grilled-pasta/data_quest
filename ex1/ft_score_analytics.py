#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_score_analytics.py                              :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:48:22 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 11:13:55 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

import sys


class GameStats(list[int]):

    @property
    def players(self) -> int:
        return len(self)

    @property
    def score(self) -> int:
        return sum(self)

    @property
    def average(self) -> float:
        return self.score / self.players if self.players > 0 else 0

    @property
    def high(self) -> int:
        return max(self) if self.players > 0 else 0

    @property
    def low(self) -> int:
        return min(self) if self.players > 0 else 0

    @property
    def score_range(self) -> int:
        return self.high - self.low

    def print_dashboard(self) -> None:
        print("=" * 40)
        print(f"{'PLAYER SCORE ANALYTICS':^40}")
        print("=" * 40)
        i = 1
        for score in self:
            print(f" PLAYER {i:.<15}{score:.>16}")
            i += 1
        print()
        print(f" {'TOTAL PLAYERS':.<22}{self.players:.>16}")
        print(f" {'TOTAL SCORE':.<22}{self.score:.>16}")
        print(f" {'AVERAGE SCORE':.<22}{self.average:.>16.2f}")
        print()
        print(f" {'HIGH SCORE':.<22}{self.high:.>16}")
        print(f" {'LOW SCORE':.<22}{self.low:.>16}")
        print(f" {'SCORE RANGE':.<22}{self.score_range:.>16}")
        print("=" * 40)


def main() -> None:
    _, *args = sys.argv
    stats: GameStats = GameStats()
    count = 0
    for arg in args:
        try:
            stats.append(int(arg))
            count += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(stats) == 0:
        print("No scores provided. Usage:",
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        stats.print_dashboard()


if __name__ == "__main__":
    main()
