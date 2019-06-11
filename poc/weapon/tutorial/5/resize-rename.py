
import PIL

from PIL import Image

import os,sys
import cv2



def rename():
    path = "C:/Users/Acer/Desktop/images-project/poc/weapon/tutorial/4/p/"
    dirs = os.listdir(path)

    pic_num = 1

    if not os.path.exists('prename'):
        os.makedirs('prename')

    for item in dirs:
        try:
            print(item)
            img = cv2.imread("p/" + item, cv2.IMREAD_GRAYSCALE)
            # resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("prename/" + str(pic_num) + ".jpg", img)
            pic_num += 1

        except Exception as e:
            print(str(e))

def resize():
    path = "C:/Users/Acer/Desktop/images-project/poc/weapon/tutorial/4/prename/"
    dirs = os.listdir(path)

    pic_num = 1

    if not os.path.exists('pp'):
        os.makedirs('pp')

    for item in dirs:
        try:
            print(item)
            img = cv2.imread("prename/" + item, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pp/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

# rename()
resize()