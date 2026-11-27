#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_data_stream.py                                  :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:49:07 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 11:27:09 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

from collections.abc import Generator
from random import choice

Event = tuple[str, str]


def get_event() -> Generator[Event]:
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release"]
    players = ["alice", "bob", "charlie", "dylan"]
    yield (choice(players), choice(actions))


def consume_event(events: list[Event]) -> Generator[Event]:
    while events:
        event = choice(events)
        events.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        player, action = next(get_event())
        print(f"Event {i}: Player {player} did event {action}")

    events = [next(get_event()) for _ in range(10)]
    print("Build list of 10 events:", events)
    for event in consume_event(events):
        print("Get event from list:", event)
        print("Remains in list:", events)


if __name__ == "__main__":
    main()
