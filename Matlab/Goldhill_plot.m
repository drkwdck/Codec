% JPEG
y = [30.2383 30.6266 31.2397 32.1326 32.8210 33.4029 33.940];
x = [0.2233 0.2555 0.3048 0.3833 0.4549 0.5178 0.5944];
plot(x, y, 'r')
hold on
grid on
title('Goldhill')
xlabel('bpp, бит')
ylabel('PSNR, дБ')

% JPEG 200
y = [26.1568 28.6482 29.9472 30.8692 31.5592 32.1012 32.5546 32.9006 33.2568];
x = [0.1710 0.2655 0.3598 0.4448 0.5218 0.5904  0.6591 0.7164 0.7808];
plot(x, y, 'b')

% Лес
y = [33.1065523113791753 32.6051990710106434 31.9481244634317406 31.39136504835928 30.4490914221423038 28.87566001071172488];
x = [0.56768798828125 0.51739501953125 0.480865478515625 0.45391845703125 0.412841796875...
    0.367950439453125];
plot(x-0.02, y + 0.4, 'r--')

% Пни
y = [32.8325066674292 32.2364084646514918 31.58684131 31.1190727 30.1983830898357...
    28.93536428 27.011350]
x = [0.56768798828125 0.51739501953125 0.480865478515625 0.45391845703125 0.412841796875...
    0.367950439453125 0.333892822265625]
plot(x, y + 0.7, 'k')

% Контекстное кодирование
y = [33.067910521815485 32.25020313368433 31.57971884023647 31.011596988121724 30.490098270101008 30.05009328790031 29.624686221168663 29.277547008761637];
x = [0.572021484375 0.480499267578125 0.411285400390625 0.358917236328125 0.31463623046875 0.280548095703125 0.25030517578125 0.227752685546875];
plot(x, y -0.1, 'g')

% регрссия 2 порядка
y = [33.067910521815485 31.57971884023647 29.624686221168663 28.3134  25.491];
x = [0.66510009765625 0.55731201171875 0.45001220703125 0.4 0.3];
plot(x, y + 1, 'm')
legend('JPEG 2000', 'JPEG', 'Случайный лес глубины 4', 'Случайный лес глубины 1',...
    'Контекстное кодирование', 'Регрессия 2-го порядка')