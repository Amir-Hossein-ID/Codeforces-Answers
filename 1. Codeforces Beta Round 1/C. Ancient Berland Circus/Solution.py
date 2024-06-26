import math

a = tuple(map(float, input().split()))
b = tuple(map(float, input().split()))
c = tuple(map(float, input().split()))

# calculate Perpendicular Bisector to determine the center
l1 = -(b[0] - a[0]) / (b[1] - a[1])
l1b = (a[1] + b[1]) / 2 - l1 * (a[0] + b[0]) / 2

l2 = -(c[0] - a[0]) / (c[1] - a[1])
l2b = (a[1] + c[1]) / 2 - l2 * (a[0] + c[0]) / 2

cx = (l2b - l1b) / (l1 - l2)
cy = l1 * cx + l1b

discenter = ((a[1] - cy) ** 2 + (a[0] - cx) ** 2) ** (1/2)

#calculate angle between three points with o being the vertex
def angle_between(a, b, o):
    return abs(math.atan2(a[1] - o[1], a[0] - o[0]) - math.atan2(b[1] - o[1], b[0] - o[0]))

ang1 = angle_between(a, b, (cx, cy))
ang2 = angle_between(a, c, (cx, cy))
ang3 = angle_between(c, b, (cx, cy))

for i in range(3, 101):
    angle_of_one = 2*math.pi / i
    if abs(ang1/angle_of_one - round(ang1/angle_of_one)) < 0.01\
        and abs(ang2/angle_of_one - round(ang2/angle_of_one)) < 0.01\
        and abs(ang3/angle_of_one - round(ang3/angle_of_one)) < 0.01:
        area_of_one = discenter * discenter * math.sin(angle_of_one) / 2
        area= area_of_one * i
        print(f'{area:.8f}')
        break
