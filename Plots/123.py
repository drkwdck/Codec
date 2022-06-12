import numpy as np

y = np.array([37.42888992393367, 36.316263555820736, 33.635984362952335, 32.69082932128259])

z = np.power(10, y / 10)

z[3] += 1000
z[2] += 850
z[1] += 350
z[0] += 280

# z[6] += 1100
# z[5] += 950
# z[4] += 600
# z[3] += 520
# z[2] += 420
# z[1] += 420
# z[0] += 250

print(np.log10(z) * 10)
