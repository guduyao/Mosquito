from PIL import Image
from PIL import ImageEnhance
import os

# # 亮度增强
# enh_bri = ImageEnhance.Brightness(image)
# brightness = 1.5
# image_brightened = enh_bri.enhance(brightness)
# image_brightened.show()
# image_brightened.save(r"F:\pycharm\ship\test\00000001.jpg")


def changeimg(imageDir):
    # 色度增强
    image = Image.open(imageDir)
    enh_col = ImageEnhance.Color(image)
    color = 2.0
    image_colored = enh_col.enhance(color)
    # image_colored.show()
    enh_sha = ImageEnhance.Sharpness(image_colored)
    sharpness2 = 4.0
    image_sharped = enh_sha.enhance(sharpness2)
    return image_sharped
    # image_sharped.show()
# 对比度增强
# enh_con = ImageEnhance.Contrast(image)
# contrast = 1.5
# image_contrasted = enh_con.enhance(contrast)
# image_contrasted.show()
# image_contrasted.save(r"F:\pycharm\ship\test\00000003.jpg")


if __name__ == '__main__':
    imageDir = "img/"  # 要改变的图片的路径文件夹
    saveDir = "test/"   # 要保存的图片的路径文件夹
    i = 0
    for name in os.listdir(imageDir):
        i = i + 1
        saveName = str(i)+".jpg"
        saveImage = changeimg(imageDir+name)
        saveImage.save(os.path.join(saveDir,saveName))

