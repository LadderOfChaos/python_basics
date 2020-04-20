import math
shirochina = float(input())

dyljina = float(input())
visochina = float(input())
astronavti_visochina = float(input())

space_needed = 2 * 2 * (astronavti_visochina + 0.4)
ship_space = shirochina * dyljina * visochina
astonaunt_caunt = ship_space/space_needed
astonaunt_caunt = (math.floor(astonaunt_caunt))
if 3 <= astonaunt_caunt <= 10:
    print(f"The spacecraft holds {astonaunt_caunt} astronauts.")
elif astonaunt_caunt < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")