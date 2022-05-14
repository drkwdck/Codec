x = imread('Lena.tif');
imwrite(uint8(x), 'NewFile.jpg', 'jpg', 'Quality', 30);
z = imread('NewFile.jpg');
PSNR = psnr(x, z)
s = dir('NewFile.jpg');
the_size = s.bytes;
bpp = 8 * the_size / 512^2
