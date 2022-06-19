from matplotlib import pyplot as plt
import numpy as np

CB91_Blue = '#2CBDFE'
CB91_Purple = '#9D2EC5'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Violet = '#ddff00'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

# jpeg
y = [27.0546, 28.2538, 31.4880, 32.5366];
x = [0.2657, 0.3589, 0.6422, 0.7592];
plt.plot(x, y, label='JPEG', color=color_list[0])

# jpeg 2000
y = [35.1452, 33.9455, 32.5490, 31.6155, 30.6306, 29.3370];
x = [0.6980, 0.5709, 0.4378, 0.3737, 0.3028, 0.2237];
plt.plot(x, y, label='JPEG 2000', color=color_list[1])

# Контекстное кодирование
y = [33.81681261336805, 33.082536422869886, 31.515783073075745, 30.266515910920017,
     28.864539027442603, 28.095877633186348]
x = [0.597808837890625, 0.53265380859375, 0.436126708984375, 0.3668212890625,
     0.29510498046875, 0.259307861328125]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = np.array([35.12056, 34.627198, 34.08088541, 33.58116081, 32.52727909, 31.97702,
              30.6849810, 30.107033, 29.950155818948067])
y -= 0.15
x = [0.685302734375, 0.619415283203125, 0.567108154296875, 0.526580810546875, 0.44244384765625,
     0.392120361328125, 0.309814453125, 0.276458740234375, 0.2674560546875]
plt.plot(x, y,  label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = np.array([35.43502, 34.98643, 34.393525, 33.8008013, 32.826004, 32.1316984608,
              30.02204])
x = [0.685302734375, 0.619415283203125, 0.567108154296875, 0.526580810546875,
     0.44244384765625, 0.392120361328125, 0.276458740234375]
y -= 0.3
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = np.array([30.1452, 31.312814, 31.770324, 33.349312, 35.080993])
y += 0.07
x = [0.350128173828125, 0.39703369140625, 0.431549072265625, 0.546539306640625, 0.72369384765625]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Barbara')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('PSNR, дБ')
plt.show()
