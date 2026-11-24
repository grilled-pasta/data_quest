# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_command_quest.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/23 19:05:47 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/23 19:24:45 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name, *args = sys.argv
    print("Program name:", program_name)
    argc = len(args)
    if argc > 0:
        print("Arguments received:", argc)
        i = 1
        for arg in args:
            print(f"Argument {i}:", arg)
            i += 1
    else:
        print("No arguments provided!")
    print("Total arguments:", argc + 1)


if __name__ == "__main__":
    main()
