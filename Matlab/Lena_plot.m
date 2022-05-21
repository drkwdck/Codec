% JPEG
y = [32.9617 33.7045 34.2822 35.1293 35.8085 36.4563];
x = [0.2293 0.2807 0.3291 0.4168 0.5051 0.6010];
plot(x, y, 'b')
hold on
grid on
title('Lena')
xlabel('bpp, бит')
ylabel('PSNR, дБ')

% JPEG 200
y = [37.4569 36.7682 36.0225 34.9903];
x = [0.4384 0.3712 0.3042 0.2239];
plot(x, y, 'r')

% Лес
y = [36.58277132050156 35.96067112662177 35.32855634237591 34.88602737671718 34.37252475178023 32.740726038061986 31.836502226888687];
x = [0.475328369140625 0.43544189453125 0.404893798828125 0.38343994140625 0.365526123046875 0.321824951171875 0.303148193359375];
plot(x - 0.02, y + 0.2, 'r--')

% Пни
y = [35.81197270 35.23129553 34.7011435925 34.239445017616 33.76916120213 32.3097685579 31.5286939750];
x = [0.475328369140625 0.43544189453125 0.404893798828125 0.38343994140625 0.365526123046875 0.321824951171875 0.303148193359375];
plot(x, y + 1.2, 'k')

% Контекстный кодер
y = [35.610938316354996, 35.083484971857054, 34.42888992393367, 33.84555990258561, 33.69079600468061, 33.17439339494001, 32.70583198522003];
x = [0.396026611328125, 0.357818603515625, 0.3162841796875, 0.28607177734375, 0.278472900390625, 0.25531005859375, 0.23583984375];
plot(x, y, 'g')

% Регрессия 2-го порядка
y = [35.42888992393367 34.316263555820736 31.635984362952335 30.69082932128259];
x = [0.494476318359375 0.413848876953125 0.316741943359375 0.296295166015625];
plot(x, y + 1.2, 'm')

legend('JPEG', 'JPEG 2000', 'Случайный лес гулбины 4',...
    'Случайный лес глубины 1', 'Контекстный кодер',...
    'Регрессия 2-го порядка')
