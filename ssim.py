from skimage.metrics import structural_similarity
from ImageProvider import ImageProvider

img1 = ImageProvider.ReadImage('TestImages/Lena.tif')
img2 = ImageProvider.ReadImage('RestoredImages/33.89_0.2568.png')
(score, diff) = structural_similarity(img2, img1, full=True)
diff = (diff * 255).astype("uint8")

# 6. You can print only the score if you want
print("SSIM: {}".format(score))