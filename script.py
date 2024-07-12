from pathlib import Path
from math import sin, cos, radians

from matplotlib import pyplot as plt

filename = "01.txt"

current_pos = (0, 0)
current_timestamp = 0
last_angle = 0

xs = []
ys = []

with Path(f"data/{filename}").open() as f:
    data = f.read()

for line in data.splitlines():
    timestamp, angle, amperage = map(int, line.split(","))

    delta = timestamp - current_timestamp
    current_timestamp = timestamp

    length = 21 * delta / 1145

    x1, y1 = current_pos
    last_angle = angle

    x2 = x1 + length * cos(radians(angle / 10))
    y2 = y1 + length * sin(radians(angle / 10))

    current_pos = (x2, y2)
    
    xs.append(x2)
    ys.append(y2)

plt.plot(xs, ys)
plt.show()
