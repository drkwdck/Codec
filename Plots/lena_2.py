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


# jpeg 2000
y = [0.9728, 0.9678, 0.9608]
x = [0.329, 0.292, 0.23]
plt.plot(x, y, label='JPEG 2000', color=color_list[1])

# Контекстное кодирование
y = [0.9628840869568428, 0.961462494633955, 0.9539078298346202]
x = [0.34893798828125, 0.33349609375, 0.27044677734375]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = [0.9583034040941771, 0.9630534051021619, 0.96711614, 0.97062801]
x = [0.293, 0.333, 0.371, 0.415]
plt.plot(x, y,  label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = [0.9600581520235162, 0.9635436235620871,  0.96757386, 0.97138868]
x = [0.3029, 0.335, 0.373, 0.42]
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = [0.9609954783117687, 0.9631372311682468, 0.96770141, 0.97062801]
x = [0.325, 0.343, 0.389, 0.4158]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Lena')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('SSIM')
plt.show()
