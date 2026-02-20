import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan2(AB, BC))

print(str(round(angle)) + "\N{DEGREE SIGN}")