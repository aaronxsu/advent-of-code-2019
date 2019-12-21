# --- Day 1: The Tyranny of the Rocket Equation ---
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?


from functools import reduce
from typing import List

MASSES: List[int] = [
    93326,
    54591,
    106194,
    129163,
    110634,
    81294,
    59548,
    77988,
    66354,
    108990,
    91097,
    102076,
    67526,
    135820,
    109167,
    94391,
    78323,
    75009,
    61836,
    55751,
    54229,
    145159,
    103821,
    136601,
    119830,
    57607,
    69157,
    115099,
    53756,
    136063,
    62243,
    111594,
    57598,
    83789,
    130669,
    67435,
    112187,
    141492,
    109872,
    84640,
    119694,
    119030,
    75716,
    119017,
    106547,
    101674,
    120137,
    93759,
    115976,
    119378,
    86245,
    93317,
    53712,
    69079,
    92125,
    62397,
    102365,
    115860,
    111618,
    65452,
    83625,
    90951,
    110774,
    114943,
    99559,
    101417,
    100651,
    98412,
    109963,
    68158,
    121405,
    85002,
    119519,
    92200,
    125104,
    71018,
    131892,
    92342,
    51671,
    94691,
    136330,
    64877,
    65449,
    65008,
    91656,
    144705,
    130867,
    74732,
    61977,
    129490,
    91928,
    109200,
    94488,
    99216,
    89115,
    89756,
    52113,
    83463,
    101765,
    62363
]


def fuel_indi(fuel: int) -> int:
    return int(fuel/3) - 2


def total_fuel_required(masses: List[int]) -> int:
    return reduce(lambda acc, fuel: acc + fuel_indi(fuel), masses, 0)


print(total_fuel_required(MASSES))
# 3152038
