from matplotlib import pyplot as plt

CB91_Blue = '#2CBDFE'
CB91_Green = '#47DBCD'
CB91_Pink = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#ddff00'
CB91_Amber = '#F5B14C'

color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber,
              CB91_Purple, CB91_Violet]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)

# jpeg
y = [27.0546, 28.2538, 31.4880, 32.5366];
x = [0.2657, 0.3589, 0.6422, 0.7592];
plt.plot(x, y, label='JPEG')

# jpeg 2000
y = [35.1452, 33.9455, 32.5490, 31.6155, 30.6306, 29.3370];
x = [0.6980, 0.5709, 0.4378, 0.3737, 0.3028, 0.2237];
plt.plot(x, y, label='JPEG 2000')

# Контекстное кодирование
y = [33.81681261336805, 33.082536422869886, 31.515783073075745, 30.266515910920017,
     28.864539027442603, 28.095877633186348];
x = [0.597808837890625, 0.53265380859375, 0.436126708984375, 0.3668212890625,
     0.29510498046875, 0.259307861328125];
plt.plot(x, y, label='Контекстное кодирование')

# Лес
y = [34.55042188853107, 33.80600151248229, 33.094401359500026, 32.33237739264571,
     30.490180338874087, 29.172589093962813, 26.241185408077722, 24.392562275736047, 23.776496202963596];
x = [0.685302734375, 0.619415283203125, 0.567108154296875, 0.526580810546875, 0.44244384765625,
     0.392120361328125, 0.309814453125, 0.276458740234375, 0.2674560546875];
plt.plot(x, y, label='Случайный лес глубины 4')

# Пни
y = [34.90722653657898, 34.236415435693196, 33.384815282699996, 32.62279131585, 30.780594262085,
     29.46300301, 24.066910126174];
x = [0.685302734375, 0.619415283203125, 0.567108154296875, 0.526580810546875,
     0.44244384765625, 0.392120361328125, 0.276458740234375];

plt.plot(x, y, label='Случайный лес глубины 1')

# регрессия
y = [28.0209927784992, 29.15372933122453, 29.7,  31.650591520825895, 33.982536422869885];
x = [0.350128173828125, 0.39703369140625, 0.431549072265625, 0.546539306640625, 0.72369384765625];
plt.plot(x, y, label='Регрессия 2-го порядка')
for i in map(lambda t: t + 1.9, y):
    print(", {0}".format(i))


plt.title('Barbara')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('PSNR, дБ')
plt.show()
