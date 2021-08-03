from PIL import Image
import os


def flip(imageDir):   #翻转图像
    img = Image.open(imageDir)
    filp_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return filp_img


def rotate90(imageDir):
    img = Image.open(imageDir)
    rotation_img = img.rotate(90)
    return rotation_img


def rotate180(imageDir):
    img = Image.open(imageDir)
    rotation_img = img.rotate(180)
    return rotation_img


def rotate270(imageDir):
    img = Image.open(imageDir)
    rotation_img = img.rotate(270)
    return rotation_img


if __name__ == '__main__':
    imageDir = "test/"
    saveDir = "pic/"
    i = 0
    for name in os.listdir(imageDir):
        i = i + 1
        saveName = str(i) + ".jpg"
        Image.open(imageDir + name).save(os.path.join(saveDir, saveName))
        i = i + 1
        saveName = str(i) + ".jpg"
        saveImage1 = flip(imageDir + name)
        saveImage1.save(os.path.join(saveDir, saveName))
        i = i + 1
        saveName = str(i) + ".jpg"
        saveImage2 = rotate90(imageDir + name)
        saveImage2.save(os.path.join(saveDir, saveName))
        i = i + 1
        saveName = str(i) + ".jpg"
        saveImage3 = rotate180(imageDir + name)
        saveImage3.save(os.path.join(saveDir, saveName))
        i = i + 1
        saveName = str(i) + ".jpg"
        saveImage4 = rotate270(imageDir + name)
        saveImage4.save(os.path.join(saveDir, saveName))
