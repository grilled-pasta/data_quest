#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_coordinate_system.py                            :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:48:38 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 10:48:44 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

import math

# Feedback: allow split(), float(), append()

Coordinates = tuple[float, float, float]


def get_player_pos() -> Coordinates:
    try:
        user_input = input(
                "Enter new coordinates as floats in format 'x,y,z':"
                )
    except EOFError:
        raise SystemExit(1)
    except KeyboardInterrupt:
        raise SystemExit(130)

    coordinates = user_input.split(",")

    if len(coordinates) != 3:
        print("Invalid syntax")
        return get_player_pos()

    values: list[float] = []

    for coordinate in coordinates:
        try:
            values.append(float(coordinate.strip()))
        except ValueError as e:
            print(f"Error on parameter '{coordinate}':", e)
            return get_player_pos()

    return (values[0], values[1], values[2])


def distance(a: Coordinates, b: Coordinates = (0, 0, 0)) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates1 = get_player_pos()
    print("Got a first set tuple:", coordinates1)
    x1, y1, z1 = coordinates1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center:  {distance(coordinates1):.4f}")
    print()
    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          f"{distance(coordinates1, coordinates2):.4f}")


if __name__ == "__main__":
    main()
