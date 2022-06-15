import numpy as np

y = np.array([0.9630534051021619, 0.9635436235620871, 0.9631372311682468,
              0.9628840869568428, 0.961462494633955,
              0.9609954783117687, 0.9600581520235162,0.9583034040941771,
              0.955711925519662, 0.9539078298346202,
              0.951478219060345, 0.9498284128640091,
              0.9472211492519603])
x = np.array([35.576727300945365, 35.65881513714713, 35.594821752442726,
              35.55368683339994, 35.32643888377345,
              35.25362687554623, 35.10416523644488, 34.834803943228,
              34.448812409476105, 34.19496801891499, 33.85998119656079,
              33.65589620807175, 33.33494404549497])

coefs = np.polyfit(x, y, deg=4)

print(coefs)
x = np.array([36.72, 36.3, 36.882,  36.228, 36.769, 36.32])
print(coefs[4]+ coefs[3] *x+ coefs[2] *x **2 + coefs[1] * x**3 + coefs[0] * x**4)