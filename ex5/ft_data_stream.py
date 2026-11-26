# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/26 01:21:11 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/26 01:54:21 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

from collections.abc import Generator
from random import choice

actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]
players = ["alice", "bob", "charlie", "dylan"]

Event = tuple[str, str]


def get_event() -> Generator[Event]:
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
