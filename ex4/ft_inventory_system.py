#!/usr/bin/env python
# *************************************************************************** #
#                                                                             #
#                                                         ::::::::            #
#    ft_inventory_system.py                             :+:    :+:            #
#                                                      +:+                    #
#    By: alkonsta <alkonsta@student.codam.nl>         +#+                     #
#                                                    +#+                      #
#    Created: 2026/11/27 10:48:57 by alkonsta      #+#    #+#                 #
#    Updated: 2026/11/27 10:49:02 by alkonsta      ########   odam.nl         #
#                                                                             #
# *************************************************************************** #

import sys


class InventoryError(Exception):
    pass


def parse_inventory() -> dict[str, int]:
    _, *args = sys.argv
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            params = arg.split(":")
            if len(params) != 2:
                raise InventoryError(f"Error - invalid parameter '{arg}'")
            item = params[0]
            if not item:
                raise InventoryError(f"Error - invalid parameter '{item}'")
            if item in inventory:
                raise InventoryError(f"Redundant item '{item}' - discarding")
            try:
                quantity = int(params[1])
                if quantity <= 0:
                    raise InventoryError(f"Error - invalid parameter '{item}'")
            except ValueError as e:
                raise InventoryError(f"Quantity error for '{params[0]}': {e}")
            inventory[item] = quantity
        except InventoryError as e:
            print(e)
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()
    if len(inventory) == 0:
        return
    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items:", total)

    for item, quantity in inventory.items():
        percentage = quantity * 100 / total if total > 0 else 0
        print(f"Item {item} represents {percentage:.1f}%")

    max_q = max(inventory.values())
    min_q = min(inventory.values())
    max_k = next(item for item, quantity in inventory.items()
                 if quantity == max_q)
    min_k = next(item for item, quantity in inventory.items()
                 if quantity == min_q)
    print(f"Item most abundant: {max_k} with quantity {min_k}")
    print(f"Item least abundant: {min_k} with quantity {min_q}")

    key, value = next(iter(inventory.items()))
    inventory[key] = value + 1
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
