from matplotlib import pyplot as plt
import numpy as np

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
y = [33.2568, 32.9006, 32.5546, 32.1012, 31.5592, 30.8692, 29.9472, 28.6482]
x = [0.7808, 0.7164, 0.6591, 0.5904, 0.5218, 0.4448, 0.3598, 0.2655]
plt.plot(x, y, label='JPEG', color=color_list[0])

# jpeg 2000
y = [35.2766, 34.3066, 33.4029, 32.8210, 32.1326, 31.2397]
x = [0.7022, 0.5672, 0.4370, 0.3740, 0.3025, 0.2239]
plt.plot(x, y, label='JPEG 2000', color=color_list[1])

# Контекстное кодирование
y = [32.967910521815485, 32.25020313368433, 31.011596988121724, 30.490098270101008, 29.624686221168663]
x = [0.463836669921875, 0.397186279296875, 0.307464599609375, 0.27386474609375, 0.223663330078125]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = np.array([34.34960683, 34.06629, 33.673516, 33.3817524, 32.88449146, 32.296597765])
x = [0.54768798828125, 0.49739501953125, 0.460865478515625, 0.43391845703125, 0.392841796875,
     0.347950439453125]
y -= 0.05
plt.plot(x, y, label='Случайный лес глубины 4', color=color_list[3])

# Пни
y = np.array([34.623541, 34.32046, 33.978055, 33.703476, 33.2529, 32.719066,
              32.13156])
x = [0.56768798828125, 0.51739501953125, 0.480865478515625, 0.45391845703125, 0.412841796875,
     0.367950439453125, 0.333892822265625]
y -= 0.05
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = [34.9352182, 33.997, 33.11232, 32.5764655710005, 31.15360]
x = [0.66510009765625, 0.55731201171875, 0.45001220703125, 0.4, 0.3]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Goldhill')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('PSNR, дБ')
plt.show()
