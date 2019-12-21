# --- Part Two - --
# During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

# Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel
# the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

# A module of mass 14 requires 2 fuel. This fuel requires no further fuel(2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel(654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
# What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

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


def fuel_required(fuel: int) -> int:
    required = fuel_indi(fuel)
    if required <= 0:
        return 0
    else:
        return required + fuel_required(required)


def all_fuel_required(masses: List[int]) -> int:
    return reduce(lambda acc, mass: acc + fuel_indi(mass) + fuel_required(fuel_indi(mass)), masses, 0)


print(all_fuel_required(MASSES))
# 4725210
