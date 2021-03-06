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
y = [0.9719, 0.9605, 0.9458, 0.9366]
x = [0.626, 0.496, 0.331, 0.3]
plt.plot(x, y, label='JPEG 2000', color=color_list[1])


# Контекстное кодирование
y = [0.9370881941923014, 0.9230100282773448, 0.9071927870748598]
x = [0.425933837890625, 0.348724365234375, 0.28521728515625]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])

# Лес
y = [0.95139118, 0.9427002317058052, 0.9330090685162458]
x = [0.5097, 0.4127, 0.351]
plt.plot(x, y,  label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = [0.95111775, 0.9421595120332129, 0.9330090685162458]
x = [0.494, 0.398, 0.3458]
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = [0.95099676, 0.941631458835123, 0.9230100282773448]
x = [0.56, 0.436, 0.333]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Goldhill')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('SSIM')
plt.show()
