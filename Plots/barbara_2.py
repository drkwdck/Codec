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
y = [0.9671, 0.9655, 0.9381]
x = [0.51, 0.479, 0.308]
plt.plot(x, y, label='JPEG 2000', color=color_list[1])


# Контекстное кодирование
y = [0.9242546526455945, 0.9373272999210159,  0.9441342420756608,
      0.9566220678633607, 0.9624026561864818]
x = [0.321868896484375, 0.37579345703125,  0.40948486328125,  0.494598388671875,  0.5501708984375]
plt.plot(x, y, label='Контекстное кодирование', color=color_list[2])


# Лес
y = np.array([0.9441342420756608, 0.9665325810093476, 0.9699495841099753])
x = [0.352, 0.56,
     0.6446533203125]
plt.plot(x, y,  label='Случа-йный лес глубины 4', color=color_list[3])

# Пни
y = np.array([0.9695347248918004, 0.9513228523226025, 0.9373272999210159])
x = [0.614, 0.4, 0.326]
plt.plot(x, y, label='Случайный лес глубины 1', color=color_list[4])

# регрессия
y = np.array([0.9689449209239337, 0.9661152636166253, 0.9624026561864818,
              0.9543178654872719, 0.9415512917328533])
x = [0.659, 0.61, 0.549, 0.466, 0.381]
plt.plot(x, y, label='Регрессия 2-го порядка', color=color_list[5])

plt.title('Barbara')
plt.grid(visible=True)
plt.legend()
plt.xlabel('bpp, бит')
plt.ylabel('SSIM')
plt.show()
