import math

AB, BC = int(input()), int(input())
denominator = math.sqrt(pow(AB, 2) + pow(BC, 2))

theta = math.degrees(math.acos(BC/denominator))
print(str(round(theta))+"°")