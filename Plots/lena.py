import numpy as np
from matplotlib import pyplot as plt

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
y = [32.9617, 33.7045, 34.2822, 35.1293, 35.8085, 36.4563]
x = [0.2293, 0.2807, 0.3291, 0.4168, 0.5051, 0.6010]
plt.plot(x, y, label='JPEG', color=color_list[0])

# jpeg 2000
y = [37.4569, 36.7682, 36.0225, 34.9903]
x = [0.4384, 0.3712, 0.3042, 0.2239]
plt.plot(x, y, label='JPEG 2000', color=color_list[1])

# Контекстное кодирование
y = [35.69161825221455, 35.381535125098154, 34.68019596866378, 33.22450114834205]
x = [0.35870361328125, 0.337188720703125, 0.29595947265625, 0.22796630859375]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = np.array([37.275277851, 36.84477061, 36.358, 36.02783, 35.7120268, 34.94827,
              34.5224])
x = [0.45532836914062497, 0.41544189453124997, 0.38489379882812497,  0.36343994140624997,
     0.34552612304687497, 0.301824951171875, 0.283148193359375]
y += 0.08
plt.plot(x, y, label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = np.array([37.58722, 37.18147,  36.70067, 36.387552, 36.06749337, 35.34289,
              35.0129839])
x = [0.475328369140625, 0.43544189453125, 0.404893798828125, 0.38343994140625, 0.365526123046875,
     0.321824951171875, 0.303148193359375]
y += 0.1
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# Регрессия
y = np.array([37.673107, 36.69484222, 35.051402, 34.6212224])
x = [0.494476318359375, 0.413848876953125, 0.316741943359375, 0.296295166015625]
y += 0.05
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Lena')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('PSNR, дБ')
plt.show()
