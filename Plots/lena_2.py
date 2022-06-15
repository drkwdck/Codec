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

# Контекстное кодирование
y = [0.9628840869568428, 0.961462494633955, 0.9539078298346202]
x = [0.34893798828125, 0.33349609375, 0.27044677734375]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = [0.9583034040941771, 0.9630534051021619, 0.96711614, 0.97038868]
x = [0.295, 0.336, 0.374, 0.414]
plt.plot(x, y,  label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = [0.9600581520235162, 0.9635436235620871,  0.96757386, 0.96980162]
x = [0.305, 0.338, 0.375, 0.401]
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = [0.96064383944227740, 0.9631372311682468, 0.96770141, 0.97062801]
x = [0.325, 0.3438, 0.391, 0.418]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Lena')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('SSIM')
plt.show()
